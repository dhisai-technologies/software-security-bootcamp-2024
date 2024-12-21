import ast
import re

class SQLInjectionParser:
    def __init__(self):
        # Define patterns to identify risky operations
        self.patterns = {
            "concatenation": re.compile(r"\+|\+=|\{\}"),
            "strcat": re.compile(r"strcat"),
            "sprintf": re.compile(r"sprintf"),
            "format": re.compile(r"[%]s|%d|.format\("),
            "f-string": re.compile(r"f\".*\""),
            "user_input": re.compile(r"input\(|get\_input\(|raw\_input\(")
        }

    def parse_file(self, filename):
        """Parse the given file and look for SQL injection risks."""
        with open(filename, "r") as file:
            code = file.read()
        self.analyze_code(code)
        
    def analyze_code(self, code):
        """Analyze the given Python code string for SQL injection risks."""
        lines = code.split("\n")
        for line_num, line in enumerate(lines, start=1):
            self.check_concatenation(line, line_num)
            self.check_strcat(line, line_num)
            self.check_sprintf(line, line_num)
            self.check_format(line, line_num)
            self.check_f_string(line, line_num)
            self.check_user_input(line, line_num)

    def check_concatenation(self, line, line_num):
        """Check for direct string concatenation in SQL queries."""
        if self.patterns["concatenation"].search(line):
            print(f"Line {line_num}: Potential concatenation vulnerability detected.")

    def check_strcat(self, line, line_num):
        """Check for usage of unsafe strcat function."""
        if self.patterns["strcat"].search(line):
            print(f"Line {line_num}: Unsafe 'strcat' function usage detected.")

    def check_sprintf(self, line, line_num):
        """Check for usage of unsafe sprintf function."""
        if self.patterns["sprintf"].search(line):
            print(f"Line {line_num}: Unsafe 'sprintf' function usage detected.")

    def check_format(self, line, line_num):
        """Check for unsafe string formatting in queries."""
        if self.patterns["format"].search(line):
            print(f"Line {line_num}: Unsafe string formatting detected (e.g., %s, .format()).")

    def check_f_string(self, line, line_num):
        """Check for usage of f-strings in SQL query construction."""
        if self.patterns["f-string"].search(line):
            print(f"Line {line_num}: Unsafe f-string usage detected in SQL query construction.")

    def check_user_input(self, line, line_num):
        """Check for direct user input without proper sanitization or parameterization."""
        if self.patterns["user_input"].search(line):
            print(f"Line {line_num}: Potential risk of SQL injection from user input without sanitization.")

# Usage Example
if __name__ == "__main__":
    parser = SQLInjectionParser()
    # Provide the path to the Python file you want to analyze
    parser.parse_file("example.py")