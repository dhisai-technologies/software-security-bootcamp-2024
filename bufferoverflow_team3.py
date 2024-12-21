import re

def detect_buffer_overflow_vulnerabilities(code, filename):
    vulnerabilities = []

    unsafe_functions = ['strcpy', 'strcat', 'gets', 'sprintf', 'scanf']
    for func in unsafe_functions:
        pattern = re.compile(rf'\b{func}\b')
        matches = pattern.finditer(code)
        for match in matches:
            vulnerability = f"Unsafe function '{func}' used in code: {filename} at line {code.count('\n', 0, match.start()) + 1}"
            vulnerabilities.append(vulnerability)
    
    fixed_size_buffers_pattern = re.compile(r'char\s+\w+\[\d+\];')
    unsafe_operations_pattern = re.compile(r'=\s*\w+\(\w+\);')

    for buffer_match in fixed_size_buffers_pattern.finditer(code):
        buffer_line = code.count('\n', 0, buffer_match.start()) + 1
        for operation_match in unsafe_operations_pattern.finditer(code[buffer_match.end():]):
            operation_line = buffer_line + code[buffer_match.end():].count('\n', 0, operation_match.start()) + 1
            vulnerabilities.append(f"Unsafe operation on fixed-size buffer in code: {filename} at line {operation_line}")

    return vulnerabilities

def test_buffer_overflow_detection():
    # Read the C test case code from the file
    with open("testcasebuffer.c", "r") as f:
        test_case_1 = f.read()
    
    print("Test Case 1: Buffer Overflow Detection")
    vulnerabilities = detect_buffer_overflow_vulnerabilities(test_case_1, "testcasebuffer.c")
    for vuln in vulnerabilities:
        print(vuln)

def main():
    test_buffer_overflow_detection()

if __name__ == '__main__':
    main()
