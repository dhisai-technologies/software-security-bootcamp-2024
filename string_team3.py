import re
import os

def detect_format_string_vulnerabilities(code, filename):
    """
    Detect format string vulnerabilities in C or C++ code.
    
    Parameters:
        code (str): The source code of the file.
        filename (str): The name of the file being analyzed.
    
    Returns:
        list: A list of vulnerabilities found in the file.
    """
    vulnerabilities = []

    # Regular expression to detect printf-like functions with user-controlled input
    pattern = r'printf\s*\(([^)]*)\)'  # Matches printf and its arguments
    matches = re.findall(pattern, code)

    for match in matches:
        # Check if dangerous format specifiers are used
        if '%n' in match:
            vulnerabilities.append(f"Warning: Use of '%n' detected in {filename}.")
        if '%x' in match:
            vulnerabilities.append(f"Warning: Use of '%x' detected in {filename}.")
        if '%p' in match:
            vulnerabilities.append(f"Warning: Use of '%p' detected in {filename}.")
        
        # Check if user-controlled input is used in printf without format specifier
        if 'printf(' in match:
            # This check is for direct usage of user input in printf without a format specifier
            if 'user_input' in match:  # Simple check for user_input in the argument list
                vulnerabilities.append(f"Warning: User-controlled input used in printf in {filename}.")
    
    return vulnerabilities

def detect_vulnerabilities_in_files(directory):
    """
    Detect format string vulnerabilities in all .c and .cpp files in a directory.
    
    Parameters:
        directory (str): The directory to scan for files.
    """
    # Get all .c and .cpp files in the directory
    files = [f for f in os.listdir(directory) if f.endswith('.c') or f.endswith('.cpp')]

    for file in files:
        with open(os.path.join(directory, file), 'r') as f:
            code = f.read()
            vulnerabilities = detect_format_string_vulnerabilities(code, file)
            if vulnerabilities:
                print(f"Vulnerabilities found in {file}:")
                for vuln in vulnerabilities:
                    print(vuln)
            else:
                print(f"No vulnerabilities found in {file}.")

def main():
    # Replace with the directory containing your .c and .cpp files
    source_code_directory = r"C:\Users\chakr\software-security-bootcamp-2024"
    detect_vulnerabilities_in_files(source_code_directory)

if __name__ == '__main__':
    main()
