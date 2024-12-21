import re

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def detect_format_string_vulnerabilities(code):
    vulnerabilities = []
    format_string_patterns = [r'printf\(', r'sprintf\(', r'%n', r'%d', r'%p']
    for pattern in format_string_patterns:
        matches = re.findall(pattern, code)
        if matches:
            vulnerabilities.append(f"Format string vulnerability detected: {matches}")
    return vulnerabilities

def detect_input_sanitization(code):
    vulnerabilities = []
    # Add patterns for missing input sanitization
    sanitization_patterns = [r'scanf\(', r'gets\(']
    for pattern in sanitization_patterns:
        matches = re.findall(pattern, code)
        if matches:
            vulnerabilities.append(f"Missing input sanitization detected: {matches}")
    return vulnerabilities

def detect_unsafe_type_casting(code):
    vulnerabilities = []
    # Add patterns for unsafe type casting
    type_casting_patterns = [r'\(int\)', r'\(char\)', r'\(float\)']
    for pattern in type_casting_patterns:
        matches = re.findall(pattern, code)
        if matches:
            vulnerabilities.append(f"Unsafe type casting detected: {matches}")
    return vulnerabilities

def detect_improper_exception_handling(code):
    vulnerabilities = []
    # Add patterns for improper exception handling
    exception_handling_patterns = [r'try\s*{', r'catch\s*\(']
    for pattern in exception_handling_patterns:
        matches = re.findall(pattern, code)
        if matches:
            vulnerabilities.append(f"Improper exception handling detected: {matches}")
    return vulnerabilities

def scan_code(file_path):
    code = read_file(file_path)
    vulnerabilities = []
    vulnerabilities.extend(detect_format_string_vulnerabilities(code))
    vulnerabilities.extend(detect_input_sanitization(code))
    vulnerabilities.extend(detect_unsafe_type_casting(code))
    vulnerabilities.extend(detect_improper_exception_handling(code))
    return vulnerabilities

if __name__ == "__main__":
    file_path = 'taj.cpp'
    vulnerabilities = scan_code(file_path)
    for vulnerability in vulnerabilities:
        print(vulnerability)
