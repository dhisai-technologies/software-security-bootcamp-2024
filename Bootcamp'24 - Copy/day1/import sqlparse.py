import sqlparse
from sqlparse.sql import Where, IdentifierList, Identifier, Comparison, TokenList
from sqlparse.tokens import Keyword, DML

class SQLQueryParser:
    def __init__(self, query):
        self.query = query
        self.parsed_query = sqlparse.parse(self.query)[0]

    def get_where_conditions(self):
        """this cmd extracts multiple WHERE conditions."""
        where_conditions = []
        for token in self.parsed_query.tokens:
            if isinstance(token, Where):
                where_conditions.extend(self._parse_conditions(token))
        return where_conditions

    def get_joins(self):
        """Extracts dynamic JOIN conditions."""
        join_conditions = []
        for token in self.parsed_query.tokens:
            if token.ttype is Keyword and "JOIN" in token.value.upper():
                join_conditions.append(str(token))
        return join_conditions

    def get_subqueries(self):
        """Extracts subqueries in the SQL statement."""
        subqueries = []
        for token in self.parsed_query.tokens:
            if token.ttype is DML and token.value.upper() == "SELECT":
                subqueries.extend(self._find_subqueries(token))
        return subqueries

    def _parse_conditions(self, where_token):
        """Helper to parse conditions inside a WHERE clause."""
        conditions = []
        for token in where_token.tokens:
            if isinstance(token, Comparison):
                conditions.append(str(token))
        return conditions

    def _find_subqueries(self, token):
        """Helper to find subqueries."""
        subqueries = []
        if isinstance(token, TokenList):
            for sub_token in token.tokens:
                if sub_token.ttype is DML and sub_token.value.upper() == "SELECT":
                    subqueries.append(str(sub_token))
                subqueries.extend(self._find_subqueries(sub_token))
        return subqueries

# Example Usage
query = """
SELECT * FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.amount > 100 AND o.date BETWEEN '2023-01-01' AND '2023-12-31'
AND EXISTS (SELECT 1 FROM payments p WHERE p.order_id = o.id AND p.status = 'Completed')
"""

parser = SQLQueryParser(query)
print("WHERE Conditions:", parser.get_where_conditions())
print("JOIN Conditions:", parser.get_joins())
print("Subqueries:", parser.get_subqueries())
