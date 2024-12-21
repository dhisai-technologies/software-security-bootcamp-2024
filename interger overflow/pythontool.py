import os
import re

# --- Integer Overflow Detection for C/C++ ---
def detect_c_cpp_overflow(code):
    overflow_detected = False
    # Regex pattern to detect operations that may cause overflow (addition, subtraction, multiplication)
    overflow_pattern = re.compile(r'(\+|\-|\*)\s*(int|long|short|unsigned|unsigned\s+int|long\s+long|unsigned\s+long)\s*\w+\s*(\+|\-|\*)\s*(int|long|short|unsigned|unsigned\s+int|long\s+long|unsigned\s+long)\s*')

    # Check for operations in the code that could potentially cause overflow
    matches = re.findall(overflow_pattern, code)
    
    if matches:
        overflow_detected = True
        print("Potential integer overflow detected in C/C++ code!")
    else:
        print("No integer overflow detected in C/C++ code.")

    return overflow_detected


# --- Main Function ---
def main():
    # User input for language (C or C++) and file path
    language = input("Enter language (C, C++): ").strip().lower()
    file_path = input("Enter the file path: ").strip()

    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found!")
        return

    # Read the content of the code file
    with open(file_path, 'r') as file:
        code = file.read()

    # Detect overflow vulnerabilities based on the language
    if language == "c" or language == "cpp":
        detect_c_cpp_overflow(code)
    else:
        print(f"Unsupported language: {language}")

if __name__ == "__main__":
    main()
