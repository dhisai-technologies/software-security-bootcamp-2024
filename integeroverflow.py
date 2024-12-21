import os
def detect_vulnerabilities(file_path):
    vulnerabilities = []
    with open(file_path, 'r') as file:
        code = file.read()
        if 'int' in code and ('+' in code or '-' in code):
            vulnerabilities.append("Potential Integer Overflow detected.")
        if 'fgets' in code and 'sizeof' in code:
            vulnerabilities.append("Potential Buffer Overflow detected.")
        if '/' in code and '0' in code:
            vulnerabilities.append("Potential Division by Zero detected.")
    return vulnerabilities
def generate_test_cases():
    test_cases = []
    test_cases.append("""
#include <stdio.h>
#include <limits.h>
int main() {
    int a = INT_MAX;
    int b = 1;
    int result = a + b; // This will cause an overflow
    printf("Result: %d\\n", result);
    return 0;
}
""")
    test_cases.append("""
#include <stdio.h>
#include <string.h>
int main() {
    char buffer[10];
    printf("Enter a string: ");
    gets(buffer); // This is unsafe and can cause buffer overflow
    printf("You entered: %s\\n", buffer);
    return 0;
}
""")
    test_cases.append("""
#include <stdio.h>

int main() {
    int a = 10;
    int b = 0;
    int result = a / b; // This will cause division by zero
    printf("Result: %d\\n", result);
    return 0;
}
""")
    return test_cases
if __name__ == "__main__":
    file_path = "software-security-bootcamp-2024/Day2/vulnerable_format_string.c"
    vulnerabilities = detect_vulnerabilities(file_path)  
    print("Detected Vulnerabilities:")
    for vulnerability in vulnerabilities:
        print(vulnerability)
    print("\nGenerated Test Cases:")
    for case in generate_test_cases():
        print(case)
