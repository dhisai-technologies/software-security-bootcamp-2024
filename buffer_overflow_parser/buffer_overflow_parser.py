import re

class BufferOverflowParser:
    def __init__(self, code):
        self.code = code
        self.issues = []

    def detect_variable_index_access(self):
        pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\s*\[\s*([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\s*\]'
        matches = re.findall(pattern, self.code)
        for match in matches:
            if match.isidentifier():
                self.issues.append(f"Potential buffer overflow: Array access with variable index '{match}'")

    def detect_loop_conditions(self):
        loop_pattern = r'\b(for|while)\s*\((.*?)\)'
        loops = re.findall(loop_pattern, self.code)
        for loop in loops:
            condition = loop[1]
            if re.search(r'\b[a-zA-Z_][a-zA-Z0-9_]*\s*>=\s*[0-9]+', condition):
                self.issues.append(f"Potential buffer overflow: Loop condition may exceed array bounds in '{condition}'")

    def detect_nested_array_access(self):
        nested_pattern = r'\b[a-zA-Z_][a-zA0-9_]*\s*\[\s*[a-zA-Z_][a-zA0-9_]*\s*\[\s*[a-zA-Z_][a-zA0-9_]*\s*\]\s*\]\s*'
        matches = re.findall(nested_pattern, self.code)
        for match in matches:
            self.issues.append(f"Potential buffer overflow: Nested array access '{match}'")

    def parse(self):
        self.detect_variable_index_access()
        self.detect_loop_conditions()
        self.detect_nested_array_access()
        return self.issues

def read_test_cases_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content.split("\n\n")

def process_all_test_cases(file_path):
    test_cases = read_test_cases_from_file(file_path)
    for i, test_case in enumerate(test_cases):
        print(f"Processing Test Case {i + 1}:")
        parser = BufferOverflowParser(test_case)
        issues = parser.parse()
        if not issues:
            print("No buffer overflow detected.")
        else:
            for issue in issues:
                print(issue)
        print("\nCode with Potential Buffer Overflow:")
        print(test_case)
        print("\n" + "="*50 + "\n")

test_file_path = r'C:\PERSONAL\test_case_file.txt'
process_all_test_cases(test_file_path)
