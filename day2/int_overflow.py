import re

def analyze_cpp_code():
    try:
        with open("test_overflow", 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return

    print("Analyzing C++ code for vulnerabilities...\n")
    vulnerabilities_found = False

    # Implicit type casting
    implicit_patterns = [
        r'\b(int|unsigned|float|double|char|short|long)\s*[^\(]*\s*=\s*\d+',  # Implicit conversion from integer to other types
        r'\b(int|unsigned|float|double|char|short|long)\s*[^\(]*\s*=\s*[^\(]*\d+',  # Implicit conversion from other types to integer
        r'\b(int|unsigned|float|double|char|short|long)\s*[^\(]*\s*=\s*[^\(]*[a-zA-Z_][a-zA-Z_0-9]*'  # Implicit conversion from other types to integer
    ]

    # Explicit type casting
    explicit_patterns = [
        r'\(int\)\s*\(\s*(unsigned|float|double|char|short|long)\s*\)',  # Explicit conversion from other types to int
        r'\(unsigned\)\s*\(\s*(int|float|double|char|short|long)\s*\)',  # Explicit conversion from other types to unsigned
        r'\(float\)\s*\(\s*(int|unsigned|double|char|short|long)\s*\)',  # Explicit conversion from other types to float
        r'\(double\)\s*\(\s*(int|unsigned|float|char|short|long)\s*\)',  # Explicit conversion from other types to double
        r'\(char\*\)\s*\(\s*(int|unsigned|float|double|short|long)\s*\)',  # Explicit conversion from other types to char*
        r'\(short\)\s*\(\s*(int|unsigned|float|double|char|long)\s*\)',  # Explicit conversion from other types to short
        r'\(long\)\s*\(\s*(int|unsigned|float|double|char|short)\s*\)'  # Explicit conversion from other types to long
    ]

    all_patterns = implicit_patterns + explicit_patterns

    for line_num, line in enumerate(lines, start=1):
        line = line.strip()
        for pattern in all_patterns:
            if re.search(pattern, line):
                print(f"Potential vulnerability detected at line {line_num}: {line}")
                vulnerabilities_found = True

    if not vulnerabilities_found:
        print("No vulnerabilities detected.")

if __name__ == "__main__":
    analyze_cpp_code()