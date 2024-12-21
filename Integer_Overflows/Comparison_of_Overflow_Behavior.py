
# ======================problem=========================
# **Comparison of Overflow Behavior:**
# Write a Python program that:
#
# 1. Accepts code snippets in C or C++.
# 2. Detects vulnerabilities  for Arithmetic (additions,
# subtraction, division, bitwise, shifts, multiplications)









# ================Explantation==============
# The provided Python script detects potential arithmetic vulnerabilities in C/C++ source code
# by analyzing common operations such as addition, subtraction, division, bitwise operations,
# shifts, and multiplication. It uses predefined regular expressions to identify patterns like
# result = a + b or result = a / b that could indicate issues such as overflow, underflow, or
# division by zero. The script reads the file, searches for these patterns, and outputs details
# for each detected vulnerability, including the operation type, file position, and matched code
# snippet. If no vulnerabilities are found, it reports the file as safe for the specified checks.
# This tool is useful for enhancing code security by automating the detection of risky arithmetic
# operations.
import re

def detect_arithmetic_vulnerabilities(file_path):
    patterns = {
        "Addition": r"\b\w+\s*=\s*\w+\s*\+\s*\w+",
        "Subtraction": r"\b\w+\s*=\s*\w+\s*-\s*\w+",
        "Division": r"\b\w+\s*=\s*\w+\s*/\s*\w+",
        "Bitwise Operation": r"\b\w+\s*=\s*\w+\s*(&|\||\^)\s*\w+",
        "Shifts": r"\b\w+\s*=\s*\w+\s*(<<|>>)\s*\w+",
        "Multiplication": r"\b\w+\s*=\s*\w+\s*\*\s*\w+"
    }

    try:
        with open(file_path, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    vulnerabilities = []
    for vuln_type, pattern in patterns.items():
        matches = re.finditer(pattern, code, re.MULTILINE)
        for match in matches:
            vulnerabilities.append((vuln_type, match.start(), match.group()))

    if vulnerabilities:
        print(f"Potential vulnerabilities found in {file_path}:")
        for vuln_type, position, usage in vulnerabilities:
            print(f"  - {vuln_type} at position {position}: {usage.strip()}")
    else:
        print(f"No vulnerabilities detected in {file_path}.")

if __name__ == "__main__":
    source_code_path = "examplecppcode.cpp" #example give cpp code
    detect_arithmetic_vulnerabilities(source_code_path)
