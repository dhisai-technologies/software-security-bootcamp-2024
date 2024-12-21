import re

def detect_vulnerable_code(file_path):
    unsafe_functions = ['strcpy', 'strcat', 'sprintf', 'gets', 'scanf']

    with open(file_path, 'r') as file:
        cpp_code = file.read()
    
    vulnerable_lines = []
    
    for func in unsafe_functions:
        pattern = re.compile(r'\b' + func + r'\s*\(')
        matches = pattern.findall(cpp_code)
        if matches:
            lines = cpp_code.split('\n')
            for i, line in enumerate(lines):
                if pattern.search(line):
                    vulnerable_lines.append((i+1, line.strip()))
    
    return vulnerable_lines

file_path = input("Please enter the path to your C++ file: ")

vulnerable_code = detect_vulnerable_code(file_path)
if vulnerable_code:
    print("Vulnerable code detected:")
    for line_number, line in vulnerable_code:
        print(f"Line {line_number}: {line}")
else:
    print("No vulnerable code detected.")
