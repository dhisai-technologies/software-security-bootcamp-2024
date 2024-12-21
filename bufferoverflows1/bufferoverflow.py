import os
import re

def detect_buffer_overflow_vulnerabilities(c_code):
    vulnerabilities = []

    # Split the code into lines to track line numbers
    lines = c_code.splitlines()

    # Check for unsafe string functions: strcpy, strcat, gets
    unsafe_functions = ["strcpy", "strcat", "gets"]
    for function in unsafe_functions:
        for line_number, line in enumerate(lines, 1):
            matches = re.finditer(r"\b" + re.escape(function) + r"\s*\(", line)
            for match in matches:
                vulnerabilities.append(f"Unsafe function '{function}' found at line {line_number}, column {match.start() + 1}: {line.strip()}")

    # Check for buffer declarations without proper bounds checking
    buffer_pattern = r"char\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\[\d+\]"  # Matches fixed-size char buffers
    for line_number, line in enumerate(lines, 1):
        buffer_matches = re.finditer(buffer_pattern, line)
        for match in buffer_matches:
            buffer_decl = match.group(0)
            buffer_name = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*", buffer_decl)[0]
            vulnerabilities.append(f"Buffer declaration without bounds checking found at line {line_number}, column {match.start() + 1}: {line.strip()}")

    # Check for array access out-of-bounds (e.g., i <= size, i >= 0)
    array_access_pattern = r"\[.*\]"  # Array access
    for line_number, line in enumerate(lines, 1):
        array_matches = re.finditer(array_access_pattern, line)
        for match in array_matches:
            array_access = match.group(0)
            if 'size' in array_access or 'strlen' in array_access:
                vulnerabilities.append(f"Possible out-of-bounds array access detected at line {line_number}, column {match.start() + 1}: {line.strip()}")

    return vulnerabilities

def analyze_test_case(file_path):
    with open(file_path, 'r') as file:
        c_code = file.read()
    vulnerabilities = detect_buffer_overflow_vulnerabilities(c_code)
    
    if vulnerabilities:
        for vuln in vulnerabilities:
            print(f"File: {file_path} - {vuln}")
    else:
        print(f"File: {file_path} - No vulnerabilities detected.")

# Main function to loop through test cases in the current directory
def main():
    for filename in os.listdir('.'):
        if filename.endswith('.c'):  # Only process C files
            analyze_test_case(filename)

if __name__ == "__main__":
    main()
