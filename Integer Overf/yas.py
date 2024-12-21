import re

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def detect_integer_overflows(code):
    vulnerabilities = []
    # Patterns for detecting potential integer overflows
    overflow_patterns = [r'\bunsigned\s+int\b', r'\bsigned\s+int\b']
    for pattern in overflow_patterns:
        matches = re.findall(pattern, code)
        if matches:
            vulnerabilities.append(f"Potential integer overflow detected: {matches}")
    return vulnerabilities

def detect_mixed_data_type_operations(code):
    vulnerabilities = []
    # Patterns for detecting mixed data type operations
    mixed_type_patterns = [r'\bint\b.*\bfloat\b', r'\bfloat\b.*\bint\b']
    for pattern in mixed_type_patterns:
        matches = re.findall(pattern, code)
        if matches:
            vulnerabilities.append(f"Mixed data type operation detected: {matches}")
    return vulnerabilities

def scan_code(file_path):
    code = read_file(file_path)
    vulnerabilities = []
    vulnerabilities.extend(detect_integer_overflows(code))
    vulnerabilities.extend(detect_mixed_data_type_operations(code))
    return vulnerabilities

if __name__ == "__main__":
    file_path = 'shu.cpp'
    vulnerabilities = scan_code(file_path)
    for vulnerability in vulnerabilities:
        print(vulnerability)
