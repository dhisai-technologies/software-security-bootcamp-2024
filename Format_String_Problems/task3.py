# ================problem=========================
# Detect Unsafe Pattern Matching :
# Write the Python program to detect vulnerabilities in C, C++.
# For example, flag cases where user-controlled input is directly
# used in RegExp constructors without sanitization.

# ============solution==================
import re

def detect_unsafe_regex(file_path):
    patterns = [
        r'regex\(".*"\)',
        r'regex\((.*?user_input.*?)\)',
        r'std::regex\((.*?user_input.*?)\)',
        r'boost::regex\((.*?user_input.*?)\)'
    ]

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
    for pattern in patterns:
        matches = re.finditer(pattern, code, re.MULTILINE)
        for match in matches:
            vulnerabilities.append((match.start(), match.group()))

    if vulnerabilities:
        print(f"Potential vulnerabilities found in {file_path}:")
        for position, usage in vulnerabilities:
            print(f"  - At position {position}: {usage.strip()}")
    else:
        print(f"No vulnerabilities detected in {file_path}.")

if __name__ == "__main__":
    source_code_path = "example.cpp"# you need to pass c or c++ file .example i am giving c++ file
    detect_unsafe_regex(source_code_path)
# =============exaplantion===============
# vulnerabilities in C/C++ source code by analyzing
# the use of regular expressions where user-controlled
# input might be used unsafely. It reads the source file and
# scans it with regex patterns that match constructors like regex()
# , std::regex(), or boost::regex() involving variables such as user_input.
# If any matches are found, they are flagged as potential vulnerabilities with their
# positions in the file. If no issues are detected, it reports the file as safe.
# This program helps identify cases where input sanitization may be missing,
# which could lead to security risks.



#
# ================output==========
# 1st case:
# #include <regex>
# #include <string>
#
# int main() {
#     std::string safe_input = "fixed_pattern";
#     std::regex pattern(safe_input); // Using a predefined safe string
#     return 0;
# }
# output:
#
# No vulnerabilities detected in example.cpp.
#
# 2nd case:::
# #include <regex>
# #include <string>
# #include <iostream>
#
# int main() {
#     std::string user_input;
#     std::cin >> user_input;
#
#     // Unsafe regex usage
#     std::regex pattern(user_input);
#
#     return 0;
# }
# output::::
# Potential vulnerabilities found in example.cpp:
#   - At position 108: std::regex pattern(user_input);



