import re
import os

def detect_integer_overflow(file_path):
    """
    Detects potential integer overflow issues in a C/C++ file and suggests mitigation steps.

    Args:
        file_path (str): Path to the C/C++ source file.

    Returns:
        None
    """
    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    # Read the file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Patterns to identify potential overflow scenarios
    patterns = [
        # Arithmetic operations with potential for overflow
        r"\bint\s+\w+\s*=\s*\w+\s*[+\-*/%]\s*\w+;",
        # Loop increment patterns
        r"for\s*\(.*;.*<\s*\w+\s*;.*\+\+\)",
        r"for\s*\(.*;.*>\s*\w+\s*;.*--\)",
        # Unsafe multiplications
        r"\b\w+\s*=\s*\w+\s*\*\s*\w+;",
        # Use of hardcoded large constants
        r"\bint\s+\w+\s*=\s*\d{10,};",
    ]

    matches = []

    # Detect patterns
    for pattern in patterns:
        matches.extend(re.findall(pattern, code))

    # If issues are detected
    if matches:
        print(f"Potential integer overflow issues detected in '{file_path}':")
        for idx, match in enumerate(matches, 1):
            print(f"  {idx}. {match}")

        print("\nMitigation steps:")
        print("  1. Use larger integer types like 'long long' or 'unsigned long long' if large values are expected.")
        print("  2. Add bounds checks before performing arithmetic operations.")
        print("  3. Use libraries like GMP (GNU Multiple Precision Arithmetic Library) for handling large numbers.")
        print("  4. Avoid hardcoding large constants; use macros or constants with appropriate type qualifiers.")
        print("  5. Be cautious with loops and ensure termination conditions are well-defined.")
    else:
        print(f"No potential integer overflow issues detected in '{file_path}'.")

# Example usage
if __name__ == "__main__":
    file_path = input("Enter the path to the C/C++ file: ").strip()
    detect_integer_overflow(file_path)
