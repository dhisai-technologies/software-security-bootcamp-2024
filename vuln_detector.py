import re

VULNERABILITIES = {
    "system": "Usage of 'system()' detected. This is a potential security risk, as it can execute arbitrary shell commands.",
    "gets": "Usage of 'gets()' detected. This is a buffer overflow risk, as it does not check for buffer size.",
    "strcpy": "Usage of 'strcpy()' detected. This is a potential buffer overflow risk, as it does not check the size of the destination buffer.",
    "sprintf": "Usage of 'sprintf()' detected. This is a potential buffer overflow risk, as it may lead to writing past the buffer limit.",
    "strcat": "Usage of 'strcat()' detected. This is a potential buffer overflow risk, as it does not check the size of the destination buffer.",
    "fopen.*'w'": "Writing to files detected using 'fopen'. Ensure that no sensitive data is being written without protection.",
    "password": "Hardcoded password detected. Avoid storing passwords directly in the code.",
    "API_KEY": "Hardcoded API key detected. Avoid storing API keys directly in the code.",
    # Arithmetic vulnerabilities
    r"\+\+|--": "Potential risk of unintended side effects with increment/decrement operators (e.g., '++' or '--').",   
    r"\b\d+\s*\+\s*\d+\b": "Potential risk of integer overflow with addition operation.",
    r"\b\d+\s*\-\s*\d*\b": "Potential risk of integer underflow with subtraction operation.",
    r"/\s*0": "Division by zero detected. This is a critical error that can cause runtime crashes.",
    r"\b\d+\s*\/\s*\d+\b": "Division operation detected, ensure no division by zero occurs.",
    r">>\s*\d{2,}": "Potential unsafe bit-shift operation detected. Ensure the shift count is within valid range for the data type.",
    r"<<\s*\d{2,}": "Potential unsafe left shift operation detected. Ensure the shift count is within valid range for the data type.",
    r"&&|\|\|": "Potential risk of unintended logical short-circuiting with logical operators.",
    r"\b\d+\s*\*\s\d+\b": "Potential risk of integer overflow with multiplication operation."
}

def scan_for_vulnerabilities(code: str, line_number: int):
    findings = []
    
    for pattern, message in VULNERABILITIES.items():
        if re.search(pattern, code, re.IGNORECASE):
            findings.append((line_number, message))
    
    return findings

def scan_code_from_file(file_name):
    with open(file_name, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            findings = scan_for_vulnerabilities(line, line_number)
            for line_num, message in findings:
                print(f"\nVulnerability detected on line {line_num}: {message}")

if __name__ == "__main__":
    scan_code_from_file('tests.c')