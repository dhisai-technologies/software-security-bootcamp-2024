import re
import os

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

def detect_vulnerabilities(code):
    vulnerabilities = []

    # Patterns for detecting unsafe printf, sprintf, and fprintf usage
    patterns = [
        r'printf\s*\(([^)]*)\)',
        r'fprintf\s*\(([^)]*)\)',
        r'sprintf\s*\(([^)]*)\)'
    ]

    for pattern in patterns:
        matches = re.findall(pattern, code)
        print(f"Pattern: {pattern}, Matches: {matches}")  # Debugging print
        for match in matches:
            print(f"Match: {match}")  # Debugging print
            if '%n' in match:
                vulnerabilities.append("Warning: Use of %n detected.")
            if '%x' in match:
                vulnerabilities.append("Warning: Use of %x detected.")
            if '%p' in match:
                vulnerabilities.append("Warning: Use of %p detected.")
    
    return vulnerabilities

filename = input("Enter the path to the C/C++ file: ")
code = read_file(filename)
unsafe_operations = detect_vulnerabilities(code)


if unsafe_operations:
    for issues in unsafe_operations:
        print(issues)

else:
    print("No Vulnerabilities found!!!")

# for issue in unsafe_operations:
#     if len(issue)==0:
#         print('No Vulnerability found for the pattern!!!')
#     else:
#         print(issue)