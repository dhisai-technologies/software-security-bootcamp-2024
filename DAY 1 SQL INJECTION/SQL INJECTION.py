import re

def detect_sql_injection(code):
    # Patterns for f-strings and %-formatting
    fstring_pattern = re.compile(r'f["\'].*SELECT.*{.*}.*["\']', re.IGNORECASE)
    percent_format_pattern = re.compile(r'["\'].*SELECT.*%.*["\']', re.IGNORECASE)

    vulnerabilities = []
    for line_no, line in enumerate(code.splitlines(), start=1):
        if fstring_pattern.search(line):
            vulnerabilities.append((line_no, "f-string formatting in query"))
        if percent_format_pattern.search(line):
            vulnerabilities.append((line_no, "%-formatting in query"))
    return vulnerabilities

def read_code_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

def main():
    file_path = 'sql 3.txt'
    code = read_code_from_file(file_path)

    if code:
        # Run detection
        results = detect_sql_injection(code)
        if results:
            for line_no, issue in results:
                print(f"Line {line_no}: {issue}")
        else:
            print("No SQL injection vulnerabilities detected.")
    
if __name__ == "__main__":
    main()
