import re

# Function to detect SQL injection vulnerabilities in C++ code
def detect_sql_injection_vulnerabilities_cpp(code):
    """
    Detects SQL injection vulnerabilities in C++ code by identifying unsafe SQL query constructions.
    """
    # Patterns for unsafe SQL query construction in C++
    patterns = [
        # Vulnerable SQL query using string concatenation ( + )
        r'\bstd::string\s+[a-zA-Z0-9_]+\s*=\s*".*"\s*\+\s*.*\+.*["\']',   
        # Vulnerable SQL query using std::to_string (f-string equivalent in C++)
        r'\bstd::string\s+[a-zA-Z0-9_]+\s*=\s*".*"\s*\+\s*std::to_string\(',   
        # Vulnerable SQL query using old-style string formatting (simulated with %)
        r'\bstd::string\s+[a-zA-Z0-9_]+\s*=\s*".*%\s*.*"',  
    ]

    # List to store vulnerabilities found
    vulnerabilities = []

    # Split code into lines and check each line
    lines = code.split('\n')
    for i, line in enumerate(lines):
        for pattern in patterns:
            if re.search(pattern, line.strip()):
                vulnerabilities.append((i + 1, line.strip()))  # Store line number and code

    return vulnerabilities

# Function to scan a C++ file for vulnerabilities
def scan_cpp_file(file_path):
    """
    Scans a C++ file for SQL injection vulnerabilities.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    
    # Detect SQL injection vulnerabilities
    vulnerabilities = detect_sql_injection_vulnerabilities_cpp(code)

    return vulnerabilities

# Main function to run the scanner
if __name__ == "__main__":
    # Path to the C++ file to scan
    cpp_file_path = "./test.cpp"  # Replace with your C++ file path

    # Run the scan
    vulnerabilities = scan_cpp_file(cpp_file_path)

    # Print the results
    if vulnerabilities:
        print("Potential SQL Injection Vulnerabilities Found in C++ File:\n")
        for line_no, line in vulnerabilities:
            print(f"  Line {line_no}: {line}")
    else:
        print("No SQL Injection Vulnerabilities Found in the C++ file.")
