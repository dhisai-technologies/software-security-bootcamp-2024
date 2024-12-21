import re

def analyze_cpp_code_for_vulnerabilities(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    vulnerabilities = []

    patterns = {
        "integer_overflow": r"(\w+)\s*=\s*\1\s*\+\s*\d+",
        "integer_underflow": r"(\w+)\s*=\s*\1\s*-\s*\d+",
        "type_conversion_issue": r"\(\s*(unsigned\s+int|unsigned\s+short|unsigned\s+char)\s*\)\s*\(\s*int\s*\)",
    }

    for vuln_type, pattern in patterns.items():
        matches = re.findall(pattern, code)
        if matches:
            for match in matches:
                vulnerabilities.append(f"{vuln_type} detected: {match}")

    if vulnerabilities:
        print("Vulnerabilities detected:")
        for vuln in vulnerabilities:
            print(vuln)
    else:
        print("No vulnerabilities detected.")

file_path = 'IntegerOverFlows.cpp' 
analyze_cpp_code_for_vulnerabilities(file_path)
