<<<<<<< HEAD
import os
import re

def find_potentially_unsanitized_code(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            code = file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

    suspicious_lines = []
    
    patterns = {
        'input': [
            r'\b(scanf|gets|fgets|getchar|std::cin)\s*[(<]',
            r'cin\s*>>\s*\w+',
            r'input\s*\(',
            r'readline\s*\(',
        ],
        'output': [
            r'\b(printf|sprintf|fprintf|snprintf|std::cout)\s*[(<]',
            r'cout\s*<<\s*\w+',
            r'system\s*\(',
            r'exec\s*\(',
        ],
        'format_string': [
            r'%[diuoxXfFeEgGaAcspn]',
            r'\{\}\.format\(',
            r'f".*\{.*\}"',
        ],
        'memory': [
            r'\b(strcpy|strcat|gets|sprintf)\s*\(',
            r'malloc\s*\(',
            r'new\s+\w+\s*\[',
        ],
        'buffer': [
            r'\[\d+\]',
            r'char\s+\w+\s*\[\d*\]',
            r'memcpy\s*\(',
        ]
    }

    lines = code.split('\n')
    
    for i, line in enumerate(lines, start=1):
        line = line.strip()
        if not line or line.startswith('//') or line.startswith('/*'):
            continue

        for category, pattern_list in patterns.items():
            for pattern in pattern_list:
                if re.search(pattern, line, re.IGNORECASE):
                    if not is_comment(lines, i-1):
                        context = get_context(lines, i-1)
                        suspicious_lines.append({
                            'line_number': i,
                            'line': line,
                            'category': category,
                            'pattern': pattern,
                            'context': context
                        })

    return suspicious_lines

def is_comment(lines, line_num):
    in_comment = False
    for i, line in enumerate(lines[:line_num+1]):
        if '/*' in line:
            in_comment = True
        if '*/' in line:
            in_comment = False
    return in_comment or lines[line_num].strip().startswith('//')

def get_context(lines, line_num, context_size=2):
    start = max(0, line_num - context_size)
    end = min(len(lines), line_num + context_size + 1)
    return lines[start:end]

def analyze_path(path):
    results = {}
    
    # Clean up the path by removing extra quotes
    path = path.strip('"\'')
    
    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        return results

    if os.path.isfile(path):
        # If it's a single file, analyze just that file
        if path.endswith(('.c', '.cpp', '.cc', '.h', '.hpp')):
            print(f"Analyzing file: {path}")
            suspicious_lines = find_potentially_unsanitized_code(path)
            if suspicious_lines:
                results[path] = suspicious_lines
        else:
            print(f"Warning: File '{path}' is not a C/C++ source file.")
    else:
        # If it's a directory, analyze all files in it
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(('.c', '.cpp', '.cc', '.h', '.hpp')):
                    file_path = os.path.join(root, file)
                    print(f"Analyzing file: {file_path}")
                    suspicious_lines = find_potentially_unsanitized_code(file_path)
                    if suspicious_lines:
                        results[file_path] = suspicious_lines
    
    return results

def main():
    import sys
    
    if len(sys.argv) < 2:
        path = input("Enter the path to the C/C++ source file or directory: ").strip()
    else:
        path = sys.argv[1]

    results = analyze_path(path)
    
    if results:
        print("\nPotentially unsanitized code found:")
        for file_path, issues in results.items():
            print(f"\nFile: {file_path}")
            for issue in issues:
                print(f"\nLine {issue['line_number']}: {issue['line']}")
                print(f"Category: {issue['category']}")
                print("Context:")
                for ctx_line in issue['context']:
                    print(f"    {ctx_line}")
                print("-" * 80)
    else:
        print("\nNo potentially unsanitized code found.")

if __name__ == "__main__":
    main()
=======
import os
import re

def find_potentially_unsanitized_code(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            code = file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

    suspicious_lines = []
    
    patterns = {
        'input': [
            r'\b(scanf|gets|fgets|getchar|std::cin)\s*[(<]',
            r'cin\s*>>\s*\w+',
            r'input\s*\(',
            r'readline\s*\(',
        ],
        'output': [
            r'\b(printf|sprintf|fprintf|snprintf|std::cout)\s*[(<]',
            r'cout\s*<<\s*\w+',
            r'system\s*\(',
            r'exec\s*\(',
        ],
        'format_string': [
            r'%[diuoxXfFeEgGaAcspn]',
            r'\{\}\.format\(',
            r'f".*\{.*\}"',
        ],
        'memory': [
            r'\b(strcpy|strcat|gets|sprintf)\s*\(',
            r'malloc\s*\(',
            r'new\s+\w+\s*\[',
        ],
        'buffer': [
            r'\[\d+\]',
            r'char\s+\w+\s*\[\d*\]',
            r'memcpy\s*\(',
        ]
    }

    lines = code.split('\n')
    
    for i, line in enumerate(lines, start=1):
        line = line.strip()
        if not line or line.startswith('//') or line.startswith('/*'):
            continue

        for category, pattern_list in patterns.items():
            for pattern in pattern_list:
                if re.search(pattern, line, re.IGNORECASE):
                    if not is_comment(lines, i-1):
                        context = get_context(lines, i-1)
                        suspicious_lines.append({
                            'line_number': i,
                            'line': line,
                            'category': category,
                            'pattern': pattern,
                            'context': context
                        })

    return suspicious_lines

def is_comment(lines, line_num):
    in_comment = False
    for i, line in enumerate(lines[:line_num+1]):
        if '/*' in line:
            in_comment = True
        if '*/' in line:
            in_comment = False
    return in_comment or lines[line_num].strip().startswith('//')

def get_context(lines, line_num, context_size=2):
    start = max(0, line_num - context_size)
    end = min(len(lines), line_num + context_size + 1)
    return lines[start:end]

def analyze_path(path):
    results = {}
    
    # Clean up the path by removing extra quotes
    path = path.strip('"\'')
    
    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        return results

    if os.path.isfile(path):
        # If it's a single file, analyze just that file
        if path.endswith(('.c', '.cpp', '.cc', '.h', '.hpp')):
            print(f"Analyzing file: {path}")
            suspicious_lines = find_potentially_unsanitized_code(path)
            if suspicious_lines:
                results[path] = suspicious_lines
        else:
            print(f"Warning: File '{path}' is not a C/C++ source file.")
    else:
        # If it's a directory, analyze all files in it
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(('.c', '.cpp', '.cc', '.h', '.hpp')):
                    file_path = os.path.join(root, file)
                    print(f"Analyzing file: {file_path}")
                    suspicious_lines = find_potentially_unsanitized_code(file_path)
                    if suspicious_lines:
                        results[file_path] = suspicious_lines
    
    return results

def main():
    import sys
    
    if len(sys.argv) < 2:
        path = input("Enter the path to the C/C++ source file or directory: ").strip()
    else:
        path = sys.argv[1]

    results = analyze_path(path)
    
    if results:
        print("\nPotentially unsanitized code found:")
        for file_path, issues in results.items():
            print(f"\nFile: {file_path}")
            for issue in issues:
                print(f"\nLine {issue['line_number']}: {issue['line']}")
                print(f"Category: {issue['category']}")
                print("Context:")
                for ctx_line in issue['context']:
                    print(f"    {ctx_line}")
                print("-" * 80)
    else:
        print("\nNo potentially unsanitized code found.")

if __name__ == "__main__":
    main()
>>>>>>> c63a4ae47a5b125c3334f4f068ed6897f6d6f2eb
