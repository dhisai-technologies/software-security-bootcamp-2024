import re
c_code = """
#include <stdio.h>

int main() {
    char account_number[20];
    char account_holder_name[50];
    char bank_details[100];

    
    gets(account_number);  
    gets(account_holder_name);  

    
    printf(account_holder_name); 
    sprintf(bank_details, account_number); 
    scanf(account_holder_name); 

    return 0;
}
"""

file_name = "bank_details_vulnerable_example.c"
with open(file_name, "w") as file:
    file.write(c_code)
print(f"Step 1: New vulnerable C code related to bank details has been saved to {file_name}")


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
