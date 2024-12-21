import re

file_path="buffer_error.cpp"
def detect_vulnerable_code(file_path):
    # List of unsafe functions to look for
    unsafe_functions = ['strcpy', 'strcat', 'gets', 'scanf', 'sprintf', 'vsprintf']
    
    vulnerabilities = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            for func in unsafe_functions:
                # Check if the unsafe function is used
                if re.search(rf'\b{func}\b', line):
                    vulnerabilities.append((i + 1, line.strip()))
    
    return vulnerabilities


cpp_file = 'buffer_error.cpp'
vulnerabilities = detect_vulnerable_code(cpp_file)

if vulnerabilities:
    print("Vulnerabilities detected:")
    for line_number, code in vulnerabilities:
        print(f"Line {line_number}: {code}")
else:
    print("No vulnerabilities detected.")
