import re
import os

def scan_format_string_vulnerabilities(code):
    vulnerabilities = []
    lines = code.splitlines()
    for i, line in enumerate(lines, start=1):
        if re.search(r'\bprintf\s*\((?!".*").*%[n|d|p|s|x|u|f|c|o].*\);', line):
            vulnerabilities.append(f"Line {i}: Potential format string vulnerability.")
    return vulnerabilities

def scan_input_sanitization(code):
    vulnerabilities = []
    lines = code.splitlines()
    for i, line in enumerate(lines, start=1):
        if re.search(r'\bgets\s*\(', line):
            vulnerabilities.append(f"Line {i}: Unsafe function 'gets' used. Consider 'fgets'.")
        if re.search(r'\bscanf\s*\(.*".*".*\)', line):
            vulnerabilities.append(f"Line {i}: Ensure proper input validation for 'scanf'.")
        if re.search(r'\bstrcpy\s*\(', line):
            vulnerabilities.append(f"Line {i}: Unsafe function 'strcpy' used. Consider 'strncpy' with size limits.")
    return vulnerabilities

def scan_unsafe_type_casting(code):
    vulnerabilities = []
    lines = code.splitlines()
    for i, line in enumerate(lines, start=1):
        if re.search(r'\(\s*\w+\s*\)\s*\w+\s*=', line):
            vulnerabilities.append(f"Line {i}: Potential unsafe type casting.")
    return vulnerabilities

def scan_improper_exception_handling(code):
    vulnerabilities = []
    if re.search(r'\btry\b', code) and not re.search(r'\bcatch\b', code):
        vulnerabilities.append("Try block without a corresponding catch block.")
    return vulnerabilities

def scan_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            code = file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []
    
    vulnerabilities = []
    vulnerabilities.extend(scan_format_string_vulnerabilities(code))
    vulnerabilities.extend(scan_input_sanitization(code))
    vulnerabilities.extend(scan_unsafe_type_casting(code))
    vulnerabilities.extend(scan_improper_exception_handling(code))
    return vulnerabilities

def main(path_to_scan):
    if os.path.isfile(path_to_scan):
        print(f"Scanning {path_to_scan}...")
        vulnerabilities = scan_file(path_to_scan)
        if vulnerabilities:
            print(f"Vulnerabilities found in {path_to_scan}:")
            for vulnerability in vulnerabilities:
                print(f" - {vulnerability}")
        else:
            print(f"No vulnerabilities found in {path_to_scan}.")
    elif os.path.isdir(path_to_scan):
        for root, _, files in os.walk(path_to_scan):
            for filename in files:
                if filename.endswith('.c') or filename.endswith('.cpp'):
                    file_path = os.path.join(root, filename)
                    print(f"Scanning {file_path}...")
                    vulnerabilities = scan_file(file_path)
                    if vulnerabilities:
                        print(f"Vulnerabilities found in {filename}:")
                        for vulnerability in vulnerabilities:
                            print(f" - {vulnerability}")
                    else:
                        print(f"No vulnerabilities found in {filename}.")
    else:
        print(f"Invalid path: {path_to_scan}")

if __name__ == "__main__":
    path_to_scan = input("Enter the file or directory to scan for C/C++ files: ").strip('"').strip("'")
    main(path_to_scan)
