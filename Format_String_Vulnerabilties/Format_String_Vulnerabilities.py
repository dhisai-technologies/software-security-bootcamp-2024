import re

def detect_format_string_vulnerabilities(code, language):
    print(f"Analyzing {language} code for format string vulnerabilities...\n")

    patterns = {
        "C": [
            r"printf\s*\(\s*\w+\s*\);",             
            r"fprintf\s*\(\s*stdout\s*,\s*\w+\);",  
            r"sprintf\s*\(\s*\w+\s*,\s*\w+\);",     
        ],
        "C++": [
            r"std::printf\s*\(\s*\w+\s*\);",        
            r"std::fprintf\s*\(\s*stdout\s*,\s*\w+\);",  
        ],
    }

    selected_patterns = patterns.get(language, [])
    if not selected_patterns:
        print(f"No patterns available for language: {language}")
        return

    vulnerabilities_found = False
    for pattern in selected_patterns:
        matches = re.findall(pattern, code)
        if matches:
            vulnerabilities_found = True
            print(f"Vulnerability Found for pattern: {pattern}")
            for match in matches:
                print(f"  -> {match}")
        else:
            print(f"No vulnerabilities found for pattern: {pattern}")

    if not vulnerabilities_found:
        print("\nNo format string vulnerabilities detected.")

print("Enter your code (C or C++) below and type 'END' at the end to analyze:")
code_input = ""
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    code_input += line + "\n"

if "#include <iostream>" in code_input or "std::" in code_input:
    language = "C++"
elif "#include <stdio.h>" in code_input:
    language = "C"
else:
    print("Unable to determine language. Defaulting to C.")
    language = "C"

detect_format_string_vulnerabilities(code_input, language)