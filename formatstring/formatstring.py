import re

def analyze_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    # Regular expressions to find potential vulnerabilities
    c_printf_pattern = r'printf\s*\(\s*([^\)]+)\s*\)'
    cpp_cout_pattern = r'std::cout\s*<<\s*([^\n]+)'

    vulnerabilities = []

    # Check for C printf vulnerabilities
    for match in re.finditer(c_printf_pattern, code):
        format_string = match.group(1)
        if re.search(r'\buser_input\b', format_string):
            vulnerabilities.append({
                'type': 'C printf',
                'line': match.start(),
                'code': match.group(0),
                'format_string': format_string.strip()
            })

    # Check for C++ cout vulnerabilities
    for match in re.finditer(cpp_cout_pattern, code):
        output_expression = match.group(1)
        if re.search(r'\buser_input\b', output_expression):
            vulnerabilities.append({
                'type': 'C++ cout',
                'line': match.start(),
                'code': match.group(0),
                'output_expression': output_expression.strip()
            })

    return vulnerabilities

def print_vulnerabilities(vulnerabilities):
    if not vulnerabilities:
        print("No vulnerabilities found.")
        return

    for vuln in vulnerabilities:
        print(f"Vulnerability Type: {vuln['type']}")
        print(f"Line Number: {vuln['line']}")
        print(f"Code: {vuln['code']}")
        if 'format_string' in vuln:
            print(f"Format String: {vuln['format_string']}")
        if 'output_expression' in vuln:
            print(f"Output Expression: {vuln['output_expression']}")
        print("-" * 40)

if __name__ == "__main__":
    # Replace 'example.c' or 'example.cpp' with the path to your C or C++ file
    file_path = 'example.c'  # Change this to your target file
    vulnerabilities = analyze_code(file_path)
    print_vulnerabilities(vulnerabilities)