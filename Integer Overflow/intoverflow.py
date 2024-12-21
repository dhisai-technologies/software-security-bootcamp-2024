import re

# Function to read C/C++ file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

# Function to detect integer overflow and underflow vulnerabilities
def detect_integer_overflow(code):
    vulnerabilities = []

    # Patterns for detecting integer operations that might cause overflow/underflow
    patterns = {
        "int_declaration": r'\bint\s+\w+\s*=\s*[^;]+;',
        "short_declaration": r'\bshort\s+\w+\s*=\s*[^;]+;',
        "long_declaration": r'\blong\s+\w+\s*=\s*[^;]+;',
        "unsigned_int_declaration": r'\bunsigned\s+int\s+\w+\s*=\s*[^;]+;',
        "unsigned_short_declaration": r'\bunsigned\s+short\s+\w+\s*=\s*[^;]+;',
        "unsigned_long_declaration": r'\bunsigned\s+long\s+\w+\s*=\s*[^;]+;',
        "arithmetic_operations": r'\b\w+\s*=\s*[^;]+[\+\-\*/][^;]+;',
        "increment_decrement": r'\b\w+\s*(\+\+|--);'
    }

    overflow_keywords = [
        r'INT_MAX', r'INT_MIN', r'SHRT_MAX', r'SHRT_MIN',
        r'LONG_MAX', r'LONG_MIN', r'UINT_MAX', r'USHRT_MAX', r'ULONG_MAX'
    ]

    def is_overflow_prone(statement):
        for keyword in overflow_keywords:
            if re.search(keyword, statement):
                return True
        return False

    for pattern_name, pattern in patterns.items():
        matches = re.findall(pattern, code)
        for match in matches:
            if pattern_name in ["arithmetic_operations", "increment_decrement"]:
                if is_overflow_prone(match) or re.search(r'\b\d{8,}\b', match) or re.search(r'0\s*-\s*\w+', match):
                    vulnerabilities.append((pattern_name, match.strip()))
            elif pattern_name in ["unsigned_int_declaration", "unsigned_short_declaration", "unsigned_long_declaration"]:
                if re.search(r'0\s*-\s*\w+', match):
                    vulnerabilities.append((pattern_name, match.strip()))
            elif is_overflow_prone(match) and (pattern_name in ["int_declaration", "short_declaration", "long_declaration"]):
                vulnerabilities.append((pattern_name, match.strip()))

    return vulnerabilities

filename = input("Enter the path to the C/C++ file: ")
code = read_file(filename)
vulnerabilities = detect_integer_overflow(code)

if vulnerabilities:
    print("The code is Vulnerable for integer overflow at below Locations:")
    for pattern_name, match in vulnerabilities:
        print(f"{pattern_name}: {match}")
else:
    print("No integer overflow/underflow vulnerabilities detected.")
