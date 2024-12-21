import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Test file content
c_code = """
#include <stdio.h>

void test_function() {
    int x = 2147483647; // Maximum value for 32-bit int
    int y = x + 1;      // Intentional overflow
    printf("Value of y: %d\\n", y);

    unsigned int z = 0;
    z = z - 1;          // Intentional underflow
    printf("Value of z: %u\\n", z);

    char a = 'A';
    int b = (int)a + 300; // Unsafe type casting
    printf("Value of b: %d\\n", b);
}

int main() {
    test_function();
    return 0;
}
"""

cpp_code = """
#include <iostream>
using namespace std;

void test_function() {
    unsigned int x = 0;
    int y = x - 1;  // Intentional underflow
    cout << "Value of y: " << y << endl;

    int maxInt = 2147483647; 
    int overflow = maxInt + 1; // Intentional overflow
    cout << "Value of overflow: " << overflow << endl;

    float z = 3.14;
    int unsafeCast = (int)z;  // Unsafe type casting
    cout << "Value of unsafeCast: " << unsafeCast << endl;
}

int main() {
    test_function();
    return 0;
}
"""

# Regex patterns for vulnerabilities
patterns = {
    "integer overflow": r"\b(int|unsigned int|short|long|long long)\b.*=.*\b2147483647\b.*[+].*",
    "integer underflow": r"\b(unsigned int|int)\b.*=.*\b0\b.*[-].*",
    "unsafe type casting": r"\((int|short|long|long long|unsigned int)\).*=.*\((char|float|double)\)"
}

def write_file(filename, content):
    """Write content to a file."""
    with open(filename, 'w') as file:
        file.write(content)
    logging.info(f"Created {filename}")

def detect_vulnerabilities(filename):
    """Detect vulnerabilities in the given file."""
    vulnerabilities = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            for vuln_type, pattern in patterns.items():
                if re.search(pattern, line):
                    logging.info(f"Matched {vuln_type}: {line.strip()}")
                    vulnerabilities.append((i + 1, vuln_type, line.strip()))
    return vulnerabilities

def main():
    # Write test files
    write_file("test.c", c_code)
    write_file("test.cpp", cpp_code)

    # Analyze files for vulnerabilities
    for filename in ["test.c", "test.cpp"]:
        logging.info(f"Analyzing {filename} for vulnerabilities...")
        vulnerabilities = detect_vulnerabilities(filename)
        if vulnerabilities:
            logging.info(f"Vulnerabilities found in {filename}:")
            for line_no, vuln_type, code in vulnerabilities:
                logging.info(f"Line {line_no}: {vuln_type} - {code}")
        else:
            logging.info(f"No vulnerabilities found in {filename}.")

if __name__ == "__main__":
    main()
