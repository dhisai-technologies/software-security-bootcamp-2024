import re

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None

def detect_integer_overflow(file_content, language):
    patterns = {
        "C++": [
            r"(int\s+\w+\s*=\s*INT_MAX;)",  # Variable assignment with INT_MAX
            r"(\w+\s*=\s*\w+\s*\+\s*\d+;)"  # Addition involving a variable
        ],
        "Java": [
            r"(int\s+\w+\s*=\s*Integer\.MAX_VALUE;)",
            r"(\w+\s*=\s*\w+\s*\+\s*\d+;)"
        ]
    }

    if language not in patterns:
        print(f"Language {language} not supported.")
        return

    overflow_detected = False
    for pattern in patterns[language]:
        if re.search(pattern, file_content):
            overflow_detected = True
            break

    if overflow_detected:
        print(f"Potential integer OVERFLOW detected in {language} code!")
    else:
        print(f"No overflow detected in {language} code.")


def detect_integer_underflow(file_content, language):
    patterns = {
        "C++": [
            r"(int\s+\w+\s*=\s*INT_MIN;)",  # Variable assignment with INT_MIN
            r"(\w+\s*=\s*\w+\s*-\s*\d+;)"  # Subtraction involving a variable
        ],
        "Java": [
            r"(int\s+\w+\s*=\s*Integer\.MIN_VALUE;)",
            r"(\w+\s*=\s*\w+\s*-\s*\d+;)"
        ]
    }

    if language not in patterns:
        print(f"Language {language} not supported.")
        return

    underflow_detected = False
    for pattern in patterns[language]:
        if re.search(pattern, file_content):
            underflow_detected = True
            break

    if underflow_detected:
        print(f"Potential integer UNDERFLOW detected in {language} code!")
    else:
        print(f"No underflow detected in {language} code.")


def detect_unsafe_cast(file_content, language):
    patterns = {
        "C++": r"\([^\)]+\)\s*[A-Za-z_]\w*",
        "Java": r"\([^\)]+\)\s*[a-zA-Z_]\w*",
    }

    if language not in patterns:
        print(f"Language {language} not supported for type cast detection.")
        return

    pattern = patterns[language]
    matches = re.findall(pattern, file_content)
    if matches:
        print(f"Potential unsafe type CASTING detected in {language} code:")
        for match in matches:
            print(f"  - {match}")
    else:
        print(f"No unsafe type casting detected in {language} code.")

if __name__ == "__main__":
    overflow_file = "overflow.cpp"
    underflow_file = "underflow.cpp"
    cast_file = "unsafetype_casting.cpp"

    overflow_content = read_file(overflow_file)
    underflow_content = read_file(underflow_file)
    cast_content = read_file(cast_file)

    if overflow_content:
        detect_integer_overflow(overflow_content, "C++")

    if underflow_content:
        detect_integer_underflow(underflow_content, "C++")

    if cast_content:
        detect_unsafe_cast(cast_content, "C++")
