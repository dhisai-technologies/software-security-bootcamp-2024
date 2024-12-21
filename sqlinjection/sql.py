import re

# Sample code to scan for SQL injection vulnerabilities
sample_code = """
def vulnerable_function(user_input):
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    execute_query(query)

def safe_function(user_input):
    query = "SELECT * FROM users WHERE username = %s"
    execute_query(query, (user_input,))
"""

def find_sql_injection_vulnerabilities(code):
    """
    Parses the given source code to identify potential SQL injection vulnerabilities.

    Args:
        code (str): The source code to analyze.

    Returns:
        list: A list of potential vulnerabilities with their line numbers.
    """
    vulnerabilities = []

    # Regular expressions for detecting vulnerabilities
    direct_concatenation_pattern = re.compile(r"\+\s*user_input")  # Direct concatenation with user input
    sql_query_pattern = re.compile(r"(SELECT|INSERT|UPDATE|DELETE)\s+.\+.")  # Usage of + operator in SQL queries
    unparameterized_query_pattern = re.compile(r"execute_query\(\s*\".\"\s\)")  # Unparameterized queries

    for i, line in enumerate(code.splitlines(), start=1):
        if direct_concatenation_pattern.search(line):
            vulnerabilities.append((i, "Direct string concatenation with user input: " + line.strip()))
        elif sql_query_pattern.search(line):
            vulnerabilities.append((i, "Usage of + operator in SQL query: " + line.strip()))
        elif unparameterized_query_pattern.search(line):
            vulnerabilities.append((i, "Unparameterized query: " + line.strip()))

    return vulnerabilities

# Analyze the sample code
vulnerabilities = find_sql_injection_vulnerabilities(sample_code)

# Report findings
if vulnerabilities:
    print("Potential SQL injection vulnerabilities found:")
    for line_number, description in vulnerabilities:
        print(f"Line {line_number}: {description}")
else:
    print("No SQL injection vulnerabilities found.")