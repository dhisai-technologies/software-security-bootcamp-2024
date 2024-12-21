import re

# Define a function to check vulnerabilities in a C file
def check_sql_injection_vulnerabilities(file_path):
    vulnerabilities = []

    # List of patterns to detect specific SQL injection vulnerabilities
    patterns = [
        (r"(\s*sprintf\(.+%s\))", "Unsafe sprintf usage (SQL Injection)"),
        (r"(\s*strcat\(.+\))", "Unsafe string concatenation with strcat"),
        (r"(\s*\".*%.*\".*\+.*)", "Direct string concatenation in SQL query"),
        (r"(\s*\".*IN.*\(%.*\))", "Unsafe IN clause with dynamic input"),
        (r"(\s*\".*'\".*\+.*)", "Unsafe table name insertion in SQL query"),
    ]

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line_number, line in enumerate(lines, start=1):
            # Check each pattern and see if it matches the line of code
            for pattern, description in patterns:
                if re.search(pattern, line):
                    vulnerabilities.append({
                        "line": line_number,
                        "code": line.strip(),
                        "vulnerability": description
                    })

    return vulnerabilities


# Function to print the vulnerabilities found in the code
def print_vulnerabilities(vulnerabilities):
    if not vulnerabilities:
        print("No SQL injection vulnerabilities found.")
    else:
        for vuln in vulnerabilities:
            print(f"Vulnerability found on line {vuln['line']}: {vuln['vulnerability']}")
            print(f"Code: {vuln['code']}\n")


# Example usage
if __name__ == "__main__":
    # Path to the C file to check
    file_path = "sqlinjection1/testcasesqlinjection.c"
    
    # Check vulnerabilities in the given file
    vulnerabilities = check_sql_injection_vulnerabilities(file_path)
    
    # Print the vulnerabilities found
    print_vulnerabilities(vulnerabilities)
