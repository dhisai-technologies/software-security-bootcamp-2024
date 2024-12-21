import re
c_code = """
#include <stdio.h>

int main() {
    char buffer[100];
    char user_input1[50];
    char user_input2[50];

    
    gets(user_input1);  
    gets(user_input2);  

    
    printf(user_input1); 
    sprintf(buffer, user_input2); 
    scanf(user_input1); 

    return 0;
}
"""

file_name = "new_vulnerable_example.c"
with open(file_name, "w") as file:
    file.write(c_code)
print(f"Step 1: New vulnerable C code has been saved to {file_name}")


def detect_format_string_vulnerabilities(file_path):
    vulnerabilities = []
    patterns = {
        'printf': re.compile(r'\bprintf\s*\(([^)]+)\)'),
        'sprintf': re.compile(r'\bsprintf\s*\(([^)]+)\)'),
        'scanf': re.compile(r'\bscanf\s*\(([^)]+)\)'),
    }
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
        for line_number, line in enumerate(lines, start=1):
            for func, pattern in patterns.items():
                match = pattern.search(line)
                if match:
                    args = match.group(1).strip()
                    if not args.startswith('"'):
                        vulnerabilities.append({
                            'line': line_number,
                            'function': func,
                            'code': line.strip(),
                            'description': f"Potential format string vulnerability in {func} on line {line_number}.",
                        })
    except Exception as e:
        print(f"Error: {e}")
    return vulnerabilities


def analyze_file(file_path):
    print(f"Analyzing file: {file_path}\n")
    vulnerabilities = detect_format_string_vulnerabilities(file_path)
    if vulnerabilities:
        print("Potential vulnerabilities detected:\n")
        for vuln in vulnerabilities:
            print(f"Line {vuln['line']}: {vuln['description']}")
            print(f"    Code: {vuln['code']}\n")
    else:
        print("No format string vulnerabilities detected.")


analyze_file(file_name)
