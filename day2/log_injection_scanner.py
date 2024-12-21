import re
import os

def scan_file_for_log_injection(file_path):
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    log_patterns = [
        r'\bprintf\((.*?);',            
        r'\bfprintf\((.*?),\s*(.*?);',   
        r'\bsyslog\((.*?);',             
        r'\blog\((.*?);'                 
    ]

    vulnerabilities = []

    for line_no, line in enumerate(lines, start=1):
        for pattern in log_patterns:
            match = re.search(pattern, line)
            if match:
                log_arguments = match.group(1).strip()
                if is_user_controlled_input(log_arguments):
                    vulnerabilities.append((line_no, line.strip()))

    return vulnerabilities

def is_user_controlled_input(log_arguments):
   
    user_inputs = ['argv', 'gets', 'scanf', 'fgets', 'read', 'stdin', 'buffer']
    return any(input_func in log_arguments for input_func in user_inputs)

def scan_directory(directory_path):
    
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(('.c', '.cpp', '.h')):
                file_path = os.path.join(root, file)
                print(f"Scanning file: {file_path}")
                vulnerabilities = scan_file_for_log_injection(file_path)
                if vulnerabilities:
                    print(f"Vulnerabilities found in {file_path}:")
                    for line_no, line in vulnerabilities:
                        print(f"  Line {line_no}: {line}")
                else:
                    print(f"No vulnerabilities found in {file_path}.\n")

def scan_single_file(file_path):
   
    print(f"Scanning file: {file_path}")
    vulnerabilities = scan_file_for_log_injection(file_path)
    if vulnerabilities:
        print(f"Vulnerabilities found in {file_path}:")
        for line_no, line in vulnerabilities:
            print(f"  Line {line_no}: {line}")
    else:
        print(f"No vulnerabilities found in {file_path}.")

if __name__ == "__main__":
    # Accept input for file or directory path
    path = input("Enter the file or directory path to scan: ").strip()
    if os.path.isdir(path):
        scan_directory(path)
    elif os.path.isfile(path):
        scan_single_file(path)
    else:
        print("Invalid path.")
