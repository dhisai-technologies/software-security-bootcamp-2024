import sys
def detect_vulnerabilities(cpp_code):
    vulnerabilities = []
    if "strcat" in cpp_code:
        vulnerabilities.append("Unsafe use of strcat detected. This can lead to buffer overflow.")
    lines = cpp_code.split('\n')
    for line in lines:
        if 'char' in line and '[' in line and '+' in line:
            vulnerabilities.append("Direct concatenation on raw buffers detected. This can lead to buffer overflow.")
    if not vulnerabilities:
        vulnerabilities.append("No vulnerable string concatenation patterns detected.")
    return vulnerabilities
filename = input("Please enter the path to the C++ file: ")
try:
    with open(filename, 'r') as cpp_file:
        cpp_code = cpp_file.read()
        vulnerabilities = detect_vulnerabilities(cpp_code)
        for vuln in vulnerabilities:
            print(vuln)
except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)