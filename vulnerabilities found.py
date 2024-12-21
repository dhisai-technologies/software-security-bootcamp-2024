import re


def detect_sql_injection_vulnerabilities_cpp(code):
    """
    Detects SQL injection vulnerabilities in C++ code by identifying unsafe SQL query constructions.
    """
    
    patterns = [
       
        r'\bstd::string\s+[a-zA-Z0-9_]+\s*=\s*".*"\s*\+\s*.*\+.*["\']',   
       
        r'\bstd::string\s+[a-zA-Z0-9_]+\s*=\s*".*"\s*\+\s*std::to_string\(',   
        
        r'\bstd::string\s+[a-zA-Z0-9_]+\s*=\s*".*%\s*.*"',  
    ]

    
    vulnerabilities = []

    
    lines = code.split('\n')
    for i, line in enumerate(lines):
        for pattern in patterns:
            if re.search(pattern, line.strip()):
                vulnerabilities.append((i + 1, line.strip()))  

    return vulnerabilities


def scan_cpp_file(file_path):
    """
    Scans a C++ file for SQL injection vulnerabilities.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    
    
    vulnerabilities = detect_sql_injection_vulnerabilities_cpp(code)

    return vulnerabilities


if __name__ == "__main__":
    
    cpp_file_path = "./test.cpp"  

    vulnerabilities = scan_cpp_file(cpp_file_path)

    
    if vulnerabilities:
        print("Potential SQL Injection Vulnerabilities Found in C++ File:\n")
        for line_no, line in vulnerabilities:
            print(f"  Line {line_no}: {line}")
    else:
        print("No SQL Injection Vulnerabilities Found in the C++ file.")
