import re
import os  # Import os for file operations

def detect_format_string_vulnerabilities(code):
    vulnerabilities = []

    # Pattern to detect function calls (printf, sprintf, etc.) with user-controlled input
    unsafe_functions = r'(printf|sprintf|fprintf|dprintf|vprintf)\s*\(([^)]*)\)'
    matches = re.findall(unsafe_functions, code)

    for match in matches:
        function_name, args = match
        # Check if user-controlled input (e.g., argv[], user_input) is directly used in the format string
        if re.search(r'\b(user_input|argv\[\d*\])\b', args):
            vulnerabilities.append(f"Warning: User-controlled input used in {function_name} function with format string at: {args.strip()}")

        # Check for dangerous format specifiers (%n, %x, %p)
        dangerous_specifiers = ['%n', '%x', '%p']
        for specifier in dangerous_specifiers:
            if specifier in args:
                vulnerabilities.append(f"Warning: Dangerous format specifier '{specifier}' used in {function_name} at: {args.strip()}")

    return vulnerabilities

def analyze_code_file(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()

        vulnerabilities = detect_format_string_vulnerabilities(code)

        if vulnerabilities:
            for vuln in vulnerabilities:
                print(f"File: {file_path} - {vuln}")
        else:
            print(f"File: {file_path} - No vulnerabilities detected.")
    except FileNotFoundError:
        print(f"File: {file_path} not found. Please check the path.")

def main():
    # Explicitly handle both C and C++ test case files
    test_case_files = ['formatstring1/testcaseformatstring.c', 'formatstring1/testcaseformatstring.cpp']  # Specify the files directly
    
    for file_name in test_case_files:
        analyze_code_file(file_name)

if __name__ == "__main__":
    main()
