import re

def detect_vulnerable_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    # Patterns to detect negative index access
    negative_index_pattern = re.compile(r'buffer\[\s*-\d+\s*\]')

    # Patterns to detect pointer arithmetic before buffer
    pointer_before_buffer_pattern = re.compile(r'char\s*\*\s*\w+\s*=\s*\w+\s*-\s*\d+;')

    vulnerabilities = []

    # Check for negative index usage
    for match in negative_index_pattern.finditer(code):
        vulnerabilities.append((match.start(), "Negative index used in buffer access"))

    # Check for pointer arithmetic pointing before the buffer
    for match in pointer_before_buffer_pattern.finditer(code):
        vulnerabilities.append((match.start(), "Pointer arithmetic before the buffer"))

    return vulnerabilities

# Example usage
file_path = "vulnerable.cpp"  # Path to the C++ file
vulnerabilities = detect_vulnerable_code(file_path)

if vulnerabilities:
    print("Vulnerabilities detected:")
    for position, description in vulnerabilities:
        print(f"Position {position}: {description}")
else:
    print("No vulnerabilities detected.")