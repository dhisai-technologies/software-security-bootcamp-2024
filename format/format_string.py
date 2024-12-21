import re
import os

def analyze_code(file_path):
    """
    Analyze C/C++ code for potential unsafe string handling
    """
    dangerous_patterns = [
        r'sprintf\s*\([^,]+,[^,]+,[^)]+\)',  # sprintf usage
        r'strcat\s*\([^,]+,[^)]+\)',         # strcat usage
        r'strcpy\s*\([^,]+,[^)]+\)',         # strcpy usage
        r'printf\s*\([^)]*%s[^)]*\)',        # Direct printf with %s
        r'cout\s*<<\s*[a-zA-Z_][a-zA-Z0-9_]*' # Direct cout with variables
    ]

    try:
        with open(file_path, 'r') as file:
            code = file.read()
            
        issues_found = []
        for pattern in dangerous_patterns:
            matches = re.finditer(pattern, code)
            for match in matches:
                issues_found.append({
                    'line': code.count('\n', 0, match.start()) + 1,
                    'pattern': match.group(),
                    'issue': 'Potential unsanitized input usage'
                })
        
        return issues_found
                
    except Exception as e:
        print(f"Error analyzing file {file_path}: {str(e)}")
        return []

def main():
    # Example usage
    test_files = [f for f in os.listdir('.') if f.endswith(('.c', '.cpp', '.h', '.hpp'))]
    
    for file in test_files:
        print(f"\nAnalyzing {file}...")
        issues = analyze_code(file)
        
        if issues:
            print(f"Found {len(issues)} potential security issues:")
            for issue in issues:
                print(f"Line {issue['line']}: {issue['issue']}")
                print(f"Code: {issue['pattern']}\n")
        else:
            print("No immediate security issues found.")

if __name__ == "__main__":
    main()
