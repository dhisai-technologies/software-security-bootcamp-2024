import os
import re
def analyze_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        pattern = r'\b(printf|sprintf|fprintf)\s*\(\s*["\']([^"\']+)["\']'
        matches = re.finditer(pattern, content)
        vulnerabilities = []
        for match in matches:
            function_name = match.group(1)
            format_string = match.group(2)
            if '%' in format_string:
                vulnerabilities.append((function_name, format_string, match.start()))
        return vulnerabilities
def analyze_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.c') or file.endswith('.cpp'): 
                file_path = os.path.join(root, file)
                vulnerabilities = analyze_file(file_path)
                if vulnerabilities:
                    print(f'\nVulnerabilities found in {file_path}:')
                    for func, fmt_str, position in vulnerabilities:
                        print(f'  - Unsafe usage of {func} with format string "{fmt_str}" at position {position}')
                else:
                    print(f'\nNo vulnerabilities found in {file_path}.')

if __name__ == '__main__':
    directory_to_analyze = input("Enter the directory to analyze for format string vulnerabilities: ").strip()
    if os.path.isdir(directory_to_analyze):
        print(f"\nAnalyzing directory: {directory_to_analyze}")
        analyze_directory(directory_to_analyze)
    else:
        print(f"\nError: The directory '{directory_to_analyze}' does not exist.")