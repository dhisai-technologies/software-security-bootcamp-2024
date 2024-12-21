import re

class LogInjectionScanner:
    def __init__(self, code):
        self.code = code
        self.issues = []

    def detect_user_input_usage(self):
        input_pattern = r'\b(scanf|fgets|getchar|cin)\s*\('
        matches = re.findall(input_pattern, self.code)
        return matches

    def detect_logging_usage(self):
        log_pattern = r'\b(printf|fprintf|log|logger)\s*\('
        matches = re.findall(log_pattern, self.code)
        return matches

    def detect_sanitization_usage(self):
        sanitize_pattern = r'\b(snprintf|sprintf|strncpy|strtok|sanitize_input)\s*\('
        matches = re.findall(sanitize_pattern, self.code)
        return matches

    def detect_format_string_specifiers(self):
        specifier_pattern = r'(\%x|\%p|\%n)'
        matches = re.findall(specifier_pattern, self.code)
        return matches

    def detect_log_injection(self):
        user_inputs = self.detect_user_input_usage()
        logging_functions = self.detect_logging_usage()
        sanitizers = self.detect_sanitization_usage()
        format_specifiers = self.detect_format_string_specifiers()

        for log_func in logging_functions:
            for input_func in user_inputs:
                if not any(sanitizer in self.code for sanitizer in sanitizers):
                    self.issues.append(f"Potential log injection: User input from '{input_func}' is logged using '{log_func}' without sanitization or format control.")
                else:
                    self.issues.append(f"Sanitization detected: User input from '{input_func}' is sanitized before being logged using '{log_func}'.")

            for specifier in format_specifiers:
                self.issues.append(f"Potential format string vulnerability: Format specifier '{specifier}' used in '{log_func}'.")

    def parse(self):
        self.detect_log_injection()
        return self.issues

def read_test_cases_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content.split("\n\n")

def process_all_test_cases(file_path):
    test_cases = read_test_cases_from_file(file_path)
    for i, test_case in enumerate(test_cases):
        print(f"Processing Test Case {i + 1}:")
        scanner = LogInjectionScanner(test_case)
        issues = scanner.parse()
        if not issues:
            print("No log injection vulnerability or sanitization issues detected.")
        else:
            for issue in issues:
                print(issue)
        print("\nCode with Potential Log Injection:")
        print(test_case)
        print("\n" + "="*50 + "\n")

test_file_path = r'C:\PERSONAL\test_case_file1.txt'
process_all_test_cases(test_file_path)
