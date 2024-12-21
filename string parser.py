import re

class StaticCodeAnalyzer:
    def __init__(self):
        # Define a regular expression to match unsafe printf usages in C and C++ code
        self.format_string_pattern = r'printf\s*\(\s*[^"]*\s*,\s*[^"]*\s*\)'

    def detect_format_string_vulnerabilities(self, code: str):
        """
        Detect format string vulnerabilities in C/C++ code by checking for unsafe printf usage.
        """
        vulnerabilities = []
        lines = code.splitlines()
        
        for line_num, line in enumerate(lines, start=1):
            # Check if there is a printf usage with potential unsafe format string
            if re.search(r'printf\s*\(\s*[^"]*\s*,\s*[^"]*\s*\)', line):
                vulnerabilities.append((line_num, line))
        
        return vulnerabilities
    
    def suggest_safer_alternatives(self, code: str):
        """
        Suggest safer alternatives to printf usages that have format string vulnerabilities.
        Replace unsafe printf(user_input) with printf("%s", user_input).
        """
        safe_code = []
        lines = code.splitlines()
        
        for line in lines:
            # If printf doesn't use a format string, replace it with the safe alternative
            if 'printf(' in line and not re.search(r'printf\s*\(\s*".*"\s*,', line):
                safe_line = re.sub(r'printf\s*\(\s*([^\)]*)\)', r'printf("%s",\1)', line)
                safe_code.append(safe_line)
            else:
                safe_code.append(line)
        
        return "\n".join(safe_code)

    def analyze_code(self, code: str):
        """
        Analyze the code for format string vulnerabilities and suggest safer alternatives.
        """
        vulnerabilities = self.detect_format_string_vulnerabilities(code)
        safe_code = self.suggest_safer_alternatives(code)
        
        return vulnerabilities, safe_code


# Sample C/C++ code to test the analyzer
sample_code = """
#include <stdio.h>

int main() {
    char user_input[100];
    scanf("%s", user_input);
    printf(user_input); // Vulnerable format string
    
    // Safe printf usage
    printf("%s", user_input); // No vulnerability
    return 0;
}
"""

# Initialize the StaticCodeAnalyzer
analyzer = StaticCodeAnalyzer()

# Run analysis
vulnerabilities, suggested_code = analyzer.analyze_code(sample_code)

# Output detected vulnerabilities
if vulnerabilities:
    print("Detected Vulnerabilities:")
    for vuln in vulnerabilities:
        print(f"Line {vuln[0]}: {vuln[1]}")

# Output suggested safer code
print("\nSuggested Safer Code:")
print(suggested_code)
