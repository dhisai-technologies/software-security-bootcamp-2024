import re

# Function to read Java file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

# Function to detect SQL injection vulnerabilities based on the defined "sins"
def detect_sql_injection_sins(code):
    if code is None:
        return

    # Patterns for detecting SQL injection vulnerabilities
    patterns = {
        "SIN 1: Direct String Concatenation": [
            r'String\s+\w+\s*=\s*".*"\s*\+\s*\w+',  # String concatenation using +
            r'\+=\s*".*"',                         # String concatenation using +=
        ],
        "SIN 2: Unsafe Buffer Operations": [
            r'strcat\s*\(.*\)',                    # strcat()
            r'sprintf\s*\(.*\)',                   # sprintf()
            r'\w+\[.*\]\s*=\s*".*"',               # Direct buffer manipulation
        ],
        "SIN 3: Dynamic Query Construction": [
            r'\w+\s*=\s*\[\]\s*;',                 # Dynamic array initialization
            r'for\s*\(.*:\s*\w+\)',                # Enhanced for loop
            r'".*"\s*\+\s*\w+',                    # Dynamic query parts with string concatenation
        ],
        "SIN 4: Unsafe List Operations": [
            r'IN\s*\(.*\)',                        # IN clause with list
        ],
        "SIN 5: Unsafe String Formatting": [
            r'f".*{.*}"',                          # f-strings in query construction
            r'".*"\s*%\s*\w+',                     # %-formatting in SQL queries
            r'".*"\s*\.format\s*\(.*\)',           # .format() method usage in queries
        ]
    }

    vulnerabilities_found = {sin: [] for sin in patterns}

    for sin, sin_patterns in patterns.items():
        for pattern in sin_patterns:
            matches = re.findall(pattern, code, re.IGNORECASE)
            if matches:
                vulnerabilities_found[sin].extend(matches)

    return vulnerabilities_found

# Main function to get user input and process the file
def main():
    filename = input("Enter the path to the Java file: ")
    java_code = read_file(filename)
    if java_code:
        vulnerabilities = detect_sql_injection_sins(java_code)
        for sin, issues in vulnerabilities.items():
            if issues:
                print(f"\n{sin} detected:\n" + "\n".join(issues))
            else:
                print(f"\nNo {sin} detected.")

if __name__ == "__main__":
    main()
