import re

def detect_vulnerabilities(file_path):
    vulnerabilities = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Patterns to detect strcpy and strncpy
    strcpy_pattern = r'\bstrcpy\s*\(\s*([^\)]+)\)'
    strncpy_pattern = r'\bstrncpy\s*\(\s*([^,]+),\s*([^,]+),\s*([^,]+)\)'
    comment_pattern = r'^\s*//'  # Ignore commented lines

    for line_number, line in enumerate(lines, start=1):
        if re.match(comment_pattern, line):  # Skip commented lines
            continue

        # Check for strcpy vulnerabilities
        if re.search(strcpy_pattern, line):
            vulnerabilities.append((line_number, 'strcpy', line.strip()))

        # Check for strncpy vulnerabilities
        strncpy_match = re.search(strncpy_pattern, line)
        if strncpy_match:
            dest, src, size = strncpy_match.groups()
            # Detect unsafe strncpy usage
            if not re.search(r'\bsizeof\s*\(\s*{}\s*\)'.format(re.escape(dest.strip())), size.strip()):
                vulnerabilities.append((line_number, 'strncpy', line.strip()))

    return vulnerabilities


# Example usage
if __name__ == "__main__":
    cpp_code = """\
#include <cstring>
void unsafeFunction(const char* input) {
    char output[10];
    strcpy(output, input); // Unsafe: No size check
    strncpy(output, input, 20); // Unsafe: Size exceeds buffer
    strncpy(output, input, sizeof(output) - 1); // Safe usage
}
"""

    # Write the input C++ code to a temporary file
    cpp_file = "temp_code.cpp"
    with open(cpp_file, 'w') as file:
        file.write(cpp_code)

    # Detect vulnerabilities
    results = detect_vulnerabilities(cpp_file)

    if results:
        print("Potential vulnerabilities detected:")
        for line_number, vuln_type, code in results:
            print(f"[{vuln_type}] on line {line_number}: {code}")
    else:
        print("No vulnerabilities detected.")
