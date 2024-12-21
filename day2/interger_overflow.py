import re

def analyze_cpp_code(file_path):
    vulnerabilities = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line_num, line in enumerate(lines, start=1):
        # Detect integer overflow or underflow
        if re.search(r'\bint\b.*=.*[+\-*/].*;', line):
            vulnerabilities.append((line_num, "Arithmetic operation in integer", line.strip()))

        # Detect array size issues
        if re.search(r'\bint\b.*\[.*\];', line):
            size_match = re.search(r'\[(.*?)\]', line)
            if size_match:
                size_expr = size_match.group(1)
                if any(op in size_expr for op in ['+', '-', '*', '/']):
                    vulnerabilities.append((line_num, "Arithmetic operation in array size", line.strip()))

        # Detect pointer arithmetic issues
        if re.search(r'\*.*=.*[+\-*/].*;', line):
            vulnerabilities.append((line_num, "Pointer arithmetic operation", line.strip()))

    return vulnerabilities

def main():
    cpp_file_path = input("Enter the path to the C++ file: ")
    vulnerabilities = analyze_cpp_code(cpp_file_path)

    if not vulnerabilities:
        print("No vulnerabilities detected.")
    else:
        print("Vulnerabilities detected:")
        for vuln in vulnerabilities:
            line_num, issue, code = vuln
            print(f"Line {line_num}: {issue}\n    Code: {code}\n")

if __name__ == "__main__":
    main()
