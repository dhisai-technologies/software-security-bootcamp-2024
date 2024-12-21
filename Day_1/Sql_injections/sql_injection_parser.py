import re
import pydoc

# Function to detect SQL Injection vulnerabilities in C++ code
def detect_sql_injection(file_path):
    try:
        # Open and read the C++ file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        print("Scanning for SQL Injection vulnerabilities...\n")
        vulnerable_lines = []
        sql_keywords = ["SELECT", "INSERT", "UPDATE", "DELETE"]  # Common SQL keywords

        # Regex pattern to detect SQL concatenation in C++ code
        pattern = r'".*(' + '|'.join(sql_keywords) + r').*" *\+.*'

        # Scan each line of the C++ code
        for i, line in enumerate(lines, 1):
            if re.search(pattern, line, re.IGNORECASE):  # Search with case insensitivity
                vulnerable_lines.append((i, line.strip()))

        # Display results if vulnerabilities are found
        if vulnerable_lines:
            print("Potential SQL Injection Vulnerabilities Detected:\n")
            for line_num, code in vulnerable_lines:
                print(f"Line {line_num}: {code}")
        else:
            print("No SQL Injection vulnerabilities detected.")
    except FileNotFoundError:
        # Handle case where the specified file does not exist
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")

# Main execution block
if __name__ == "__main__":
    file_path = "vulnerable_code.cpp"  # Path to your C++ file
    detect_sql_injection(file_path)
pydoc.writedoc('sql_injection_parser')
