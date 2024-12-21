import re

def detect_sql_injection_vulnerabilities(code, filename):
    vulnerabilities = []

    # 1. Direct String Concatenation with User Input (Detects concatenation in SQL queries)
    concat_pattern = re.compile(r'([\w\d\(\)\.\-\_]+(?:\s*)[\+\-]\s*[\w\d\(\)\.\-\_]+)')
    # 2. Usage of '+' operator for SQL queries (Detects usage of '+' in SQL construction)
    plus_operator_pattern = re.compile(r'([\w\d\(\)\.\-\_]+)\s*\+\s*([\w\d\(\)\.\-\_]+)')
    # 3. Unparameterized Queries (Detects SQL queries with direct user input)
    unparameterized_pattern = re.compile(r'SELECT.*FROM.*WHERE.*=.*[a-zA-Z0-9]+')

    # Read the code line by line to detect the vulnerabilities at specific lines
    for line_num, line in enumerate(code.splitlines(), 1):
        # Check for Direct String Concatenation vulnerability
        matches = concat_pattern.finditer(line)
        for match in matches:
            vulnerable_code = match.group(0)
            vulnerabilities.append(f"Direct string concatenation detected at line {line_num}: '{vulnerable_code}' in code: {filename}")
        
        # Check for Usage of '+' operator vulnerability
        matches = plus_operator_pattern.finditer(line)
        for match in matches:
            vulnerable_code = match.group(0)
            vulnerabilities.append(f"Usage of '+' operator detected at line {line_num}: '{vulnerable_code}' in code: {filename}")
        
        # Check for Unparameterized Query vulnerability
        matches = unparameterized_pattern.finditer(line)
        for match in matches:
            vulnerable_code = match.group(0)
            vulnerabilities.append(f"Unparameterized query detected at line {line_num}: '{vulnerable_code}' in code: {filename}")

    return vulnerabilities

def test_sql_injection_cases():
    # Test case 1: Direct String Concatenation (Vulnerable code with user input)
    test_case_1 = """
    username = input("Enter username: ")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    """
    print("Test Case 1: Direct String Concatenation")
    vulnerabilities = detect_sql_injection_vulnerabilities(test_case_1, "Test Case 1")
    for vuln in vulnerabilities:
        print(vuln)

    # Test case 2: Usage of '+' operator for SQL queries
    test_case_2 = """
    password = input("Enter password: ")
    query = "SELECT * FROM users WHERE username = 'admin' AND password = '" + password + "'"
    """
    print("\nTest Case 2: Usage of '+' Operator")
    vulnerabilities = detect_sql_injection_vulnerabilities(test_case_2, "Test Case 2")
    for vuln in vulnerabilities:
        print(vuln)

    # Test case 3: Unparameterized SQL query with direct user input
    test_case_3 = """
    user_id = input("Enter user ID: ")
    query = "SELECT * FROM users WHERE id = " + user_id
    """
    print("\nTest Case 3: Unparameterized Query")
    vulnerabilities = detect_sql_injection_vulnerabilities(test_case_3, "Test Case 3")
    for vuln in vulnerabilities:
        print(vuln)

def main():
    test_sql_injection_cases()

if __name__ == '__main__':
    main()
