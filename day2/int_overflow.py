def analyze_cpp_code():
    try:
        with open("test_overflow", 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return

    print("Analyzing C++ code for vulnerabilities...\n")
    vulnerabilities_found = False

    for line_num, line in enumerate(lines, start=1):
        line = line.strip()

        # Check for potential integer overflow
        if "INT_MAX" in line and ("+" in line or "*" in line):
            print(f"Potential integer overflow at line {line_num}: {line}")
            vulnerabilities_found = True

        # Check for potential integer underflow
        if "INT_MIN" in line and ("-" in line or "/" in line):
            print(f"Potential integer underflow at line {line_num}: {line}")
            vulnerabilities_found = True

        # Check for potential type conversion vulnerabilities
        if "(int)" in line and ("unsigned" in line or "size_t" in line):
            print(f"Potential type conversion vulnerability (signed/unsigned mismatch) at line {line_num}: {line}")
            vulnerabilities_found = True
        elif "(unsigned)" in line and ("int" in line or "long" in line):
            print(f"Potential type conversion vulnerability (signed/unsigned mismatch) at line {line_num}: {line}")
            vulnerabilities_found = True
        elif "(char*)" in line and ("int" in line or "long" in line):
            print(f"Potential type conversion vulnerability (pointer type mismatch) at line {line_num}: {line}")
            vulnerabilities_found = True
            
    if not vulnerabilities_found:
        print("No vulnerabilities detected.")


if __name__ == "__main__":
    analyze_cpp_code()
