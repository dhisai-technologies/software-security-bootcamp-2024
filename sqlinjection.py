import re

class SQLInjectionRiskParser:
    def __init__(self, sql_query):
        self.sql_query = sql_query

    def analyze_in_clauses(self):
        # Regex to find IN clauses
        in_clause_pattern = r"\bIN\s*\((.*?)\)"
        matches = re.findall(in_clause_pattern, self.sql_query, re.IGNORECASE)

        risks = []
        for match in matches:
            # Analyze each match for risks
            risk_info = self.analyze_in_clause(match)
            if risk_info:
                risks.append(risk_info)

        return risks

    def analyze_in_clause(self, clause):
        # Check for dynamic list construction
        if self.is_dynamic_list(clause):
            return f"Risk: Dynamic list construction detected in IN clause: ({clause})"

        # Check for array parameter handling
        if self.is_array_parameter(clause):
            return f"Risk: Array parameter handling detected in IN clause: ({clause})"

        # Check for string concatenation
        if self.is_string_concatenation(clause):
            return f"Risk: String concatenation detected in IN clause: ({clause})"

        return None

    def is_dynamic_list(self, clause):
        # Check for dynamic list construction (e.g., using variables)
        dynamic_pattern = r"\b\w+\s*=\s*.*"
        return bool(re.search(dynamic_pattern, clause))

    def is_array_parameter(self, clause):
        # Check for array parameter handling (e.g., using array syntax)
        array_pattern = r"\bARRAY\s*\(\s*.*?\s*\)"
        return bool(re.search(array_pattern, clause))

    def is_string_concatenation(self, clause):
        # Check for string concatenation (e.g., using + or ||)
        concatenation_pattern = r"(\+|\|\|)"
        return bool(re.search(concatenation_pattern, clause))

file = open("testcase.txt" , "r")
content = file.read()
file.close()

parser = SQLInjectionRiskParser(content)
risks = parser.analyze_in_clauses()

for risk in risks:
    print(risk)