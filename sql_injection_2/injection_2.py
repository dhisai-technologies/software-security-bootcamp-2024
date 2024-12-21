import re

# Function to check for multiple WHERE conditions (AND/OR)
def check_multiple_where_conditions(query):
    # This regex will find multiple conditions in the WHERE clause (AND/OR)
    if re.search(r'WHERE.(\bAND\b|\bOR\b).(\bAND\b|\bOR\b)', query, re.IGNORECASE):
        print("Found multiple WHERE conditions.")

# Function to check for dynamic JOIN conditions
def check_dynamic_joins(query):
    # This regex looks for multiple JOIN or LEFT JOIN clauses in the query
    if len(re.findall(r'\bJOIN\b|\bLEFT JOIN\b', query, re.IGNORECASE)) > 1:
        print("Found dynamic JOIN conditions.")

# Function to check for subquery constructions (nested SELECTs)
def check_subqueries(query):
    # This regex looks for subqueries (nested SELECT statements)
    if re.search(r'\(SELECT.*\)', query, re.IGNORECASE):
        print("Found subquery construction.")

# Function to parse the file and check each query
def analyze_queries(file_path):
    with open(file_path, 'r') as file:
        queries = file.read().split(';')  # Split queries based on semicolon
        
        for query in queries:
            if query.strip():  # Ignore empty queries
                print("\nAnalyzing query:")
                print(query.strip())
                
                # Check for multiple WHERE conditions
                check_multiple_where_conditions(query)
                
                # Check for dynamic JOIN conditions
                check_dynamic_joins(query)
                
                # Check for subqueries
                check_subqueries(query)

# Specify the path to your SQL file
file_path = 'input.sql'

# Analyze the queries from the file
analyze_queries(file_path)