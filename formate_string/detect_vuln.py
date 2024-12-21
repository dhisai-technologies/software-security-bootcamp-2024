import os
import re

# Define patterns for C and C++ functions and unsafe format specifiers
PATTERNS = {
    "C": [
        r"\bprintf\s*\(([^)]+)\)",
        r"\bsprintf\s*\(([^)]+)\)",
        r"\bsnprintf\s*\(([^)]+)\)",
        r"\bfprintf\s*\(([^)]+)\)",
    ],
    "C++": [
        r"\bstd::printf\s*\(([^)]+)\)",
        r"\bstd::sprintf\s*\(([^)]+)\)",
        r"\bstd::snprintf\s*\(([^)]+)\)",
        r"\bstd::fprintf\s*\(([^)]+)\)",
    ],
    "Unsafe Specifiers": [
        r"%n",
        r"%p",
        r"%d",
        r"%s",
    ],
}

def analyze_file(file_path):
    """
    Analyzes a single file for format string vulnerabilities.
    """
    if not os.path.isfile(file_path):
        print(f"[Error] File not found: {file_path}")
        return

    # Determine the file type (C or C++) based on extension
    if file_path.endswith(".c"):
        language = "C"
    elif file_path.endswith(".cpp"):
        language = "C++"
    else:
        print(f"[Skipped] Unsupported file type: {file_path}")
        return

    # Read file content
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    print(f"Analyzing {file_path} ({language})...\n")

    # Search for function usage patterns
    for pattern in PATTERNS[language]:
        matches = re.finditer(pattern, content)
        for match in matches:
            func_usage = match.group()
            print(f"[Potential Issue] {language} Function Usage: {func_usage} at position {match.start()}")

    # Search for unsafe specifiers
    for pattern in PATTERNS["Unsafe Specifiers"]:
        matches = re.finditer(pattern, content)
        for match in matches:
            unsafe_specifier = match.group()
            print(f"[Unsafe Specifier] Found {unsafe_specifier} at position {match.start()}")

    print(f"Finished analyzing {file_path}\n")

def analyze_directory(directory_path):
    """
    Recursively analyzes all C and C++ files in a directory for format string vulnerabilities.
    """
    if not os.path.isdir(directory_path):
        print(f"[Error] Directory not found: {directory_path}")
        return

    print(f"Starting analysis in directory: {directory_path}\n")
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".c") or file.endswith(".cpp"):
                analyze_file(os.path.join(root, file))

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python detect_vuln.py <file_or_directory>")
        sys.exit(1)

    target = sys.argv[1]

    if os.path.isdir(target):
        analyze_directory(target)
    elif os.path.isfile(target):
        analyze_file(target)
    else:
        print(f"[Error] Invalid path: {target}")
