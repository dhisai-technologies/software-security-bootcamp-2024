import re

class CppVulnerabilityAnalyzer:
    def __init__(self):
        self.vulnerabilities = []

    def analyze(self):
        with open("testcase4.txt", "r") as file:
            code = file.read()
        self.check_integer_overflow(code)
        self.check_integer_underflow(code)
        self.check_type_conversion(code)

    def check_integer_overflow(self, code):
        overflow_patterns = [
            r'\b(\w+)\s*=\s*(\w+)\s*\+\s*(\w+)', 
            r'\b(\w+)\s*=\s*(\w+)\s*\*\s*(\w+)',
        ]
        for pattern in overflow_patterns:
            matches = re.findall(pattern, code)
            if matches:
                self.vulnerabilities.append("Potential integer overflow detected.")

    def check_integer_underflow(self, code):
        underflow_patterns = [
            r'\b(\w+)\s*=\s*(\w+)\s*-\s*(\w+)',
        ]
        for pattern in underflow_patterns:
            matches = re.findall(pattern, code)
            if matches:
                self.vulnerabilities.append("Potential integer underflow detected.")

    def check_type_conversion(self, code):
        conversion_patterns = [
            r'\bstatic_cast<\w+>\s*\(\s*\w+\s*\)',
            r'\b(\w+)\s*=\s*\(\w+\)\s*(\w+)', 
        ]
        for pattern in conversion_patterns:
            matches = re.findall(pattern, code)
            if matches:
                self.vulnerabilities.append("Potential type conversion issue detected.")

    def output_results(self):
        if self.vulnerabilities:
            print("Detected Vulnerabilities:")
            for vulnerability in self.vulnerabilities:
                print(f"- {vulnerability}")
        else:
            print("No vulnerabilities detected.")

def main(): 
    analyzer = CppVulnerabilityAnalyzer()
    analyzer.analyze()
    analyzer.output_results()

if __name__ == "__main__":
    main()