import re

def detect_integer_overflow(file_content, language):
    # Define patterns for various operations that may cause overflow
    patterns = {
        "C": {
            "addition": r"\b(\w+)\s*=\s*\1\s*\+\s*(\d+|\w+)",  # x = x + y
            "subtraction": r"\b(\w+)\s*=\s*\1\s*-\s*(\d+|\w+)",  # x = x - y
            "multiplication": r"\b(\w+)\s*=\s*\1\s*\*\s*(\d+|\w+)",  # x = x * y
            "division": r"\b(\w+)\s*=\s*\1\s*/\s*(\d+|\w+)",  # x = x / y
            "bitwise_and": r"\b(\w+)\s*=\s*\1\s*&\s*(\d+|\w+)",  # x = x & y
            "bitwise_or": r"\b(\w+)\s*=\s*\1\s*\|\s*(\d+|\w+)",  # x = x | y
            "bitwise_xor": r"\b(\w+)\s*=\s*\1\s*\^\s*(\d+|\w+)",  # x = x ^ y
            "left_shift": r"\b(\w+)\s*=\s*\1\s*<<\s*(\d+|\w+)",  # x = x << y
            "right_shift": r"\b(\w+)\s*=\s*\1\s*>>\s*(\d+|\w+)",  # x = x >> y
        },
        "C++": {
            "addition": r"\b(\w+)\s*=\s*\1\s*\+\s*(\d+|\w+)",  # x = x + y
            "subtraction": r"\b(\w+)\s*=\s*\1\s*-\s*(\d+|\w+)",  # x = x - y
            "multiplication": r"\b(\w+)\s*=\s*\1\s*\*\s*(\d+|\w+)",  # x = x * y
            "division": r"\b(\w+)\s*=\s*\1\s*/\s*(\d+|\w+)",  # x = x / y
            "bitwise_and": r"\b(\w+)\s*=\s*\1\s*&\s*(\d+|\w+)",  # x = x & y
            "bitwise_or": r"\b(\w+)\s*=\s*\1\s*\|\s*(\d+|\w+)",  # x = x | y
            "bitwise_xor": r"\b(\w+)\s*=\s*\1\s*\^\s*(\d+|\w+)",  # x = x ^ y
            "left_shift": r"\b(\w+)\s*=\s*\1\s*<<\s*(\d+|\w+)",  # x = x << y
            "right_shift": r"\b(\w+)\s*=\s*\1\s*>>\s*(\d+|\w+)",  # x = x >> y
        }
    }

    # Check for potential overflows in the file content
    for line_number, line in enumerate(file_content.splitlines(), start=1):
        for operation, pattern in patterns[language].items():
            if re.search(pattern, line):
                print(f"Potential integer overflow detected in {operation} operation on line {line_number} in {language} code!")

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

if __name__ == "__main__":
    # Paths to the test case files
    c_file_path = 'integeroverflows1/testcaseintegeroverflow.c'
    cpp_file_path = 'integeroverflows1/testcaseintegeroverflow.cpp'

    # Read and analyze C test case
    c_code = read_file(c_file_path)
    detect_integer_overflow(c_code, "C")

    # Read and analyze C++ test case
    cpp_code = read_file(cpp_file_path)
    detect_integer_overflow(cpp_code, "C++")