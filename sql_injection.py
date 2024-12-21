import re
import os

class MemoryUsageAnalyzer:
    def __init__(self):
        self.malloc_pattern = re.compile(r'\bmalloc\((.*?)\)')
        self.calloc_pattern = re.compile(r'\bcalloc\((.*?),\s?(.*?)\)')
        self.pointer_arithmetic_pattern = re.compile(r'(\w+)\s?\+\s?(\d+)')
        self.memory_access_pattern = re.compile(r'(\w+)\[(.*?)\]')

    def analyze_file(self, filename):
        if not os.path.isfile(filename):
            print(f"Error: The file '{filename}' was not found.")
            return

        with open(filename, 'r') as file:
            lines = file.readlines()

        for line_number, line in enumerate(lines, start=1):
            self.check_malloc(line, line_number)
            self.check_calloc(line, line_number)
            self.check_pointer_arithmetic(line, line_number)
            self.check_memory_access(line, line_number)

    def check_malloc(self, line, line_number):
        match = self.malloc_pattern.search(line)
        if match:
            size_expression = match.group(1)
            if not re.search(r'sizeof\(\w+\)', size_expression):
                print(f"Line {line_number}: Potential unsafe malloc size calculation -> {line.strip()}")

    def check_calloc(self, line, line_number):
        match = self.calloc_pattern.search(line)
        if match:
            num_elements, element_size = match.groups()
            if not re.search(r'sizeof\(\w+\)', element_size):
                print(f"Line {line_number}: Potential unsafe calloc usage -> {line.strip()}")

    def check_pointer_arithmetic(self, line, line_number):
        match = self.pointer_arithmetic_pattern.search(line)
        if match:
            print(f"Line {line_number}: Potential pointer arithmetic issue -> {line.strip()}")

    def check_memory_access(self, line, line_number):
        match = self.memory_access_pattern.search(line)
        if match:
            variable, index_expression = match.groups()
            try:
                index = int(index_expression)
                if index < 0:
                    print(f"Line {line_number}: Negative index access in variable '{variable}' -> {line.strip()}")
            except ValueError:
                print(f"Line {line_number}: Non-integer index or potential out-of-bounds access -> {line.strip()}")

if __name__ == "__main__":
    filename = 'test.c'  # Replace with your C source file
    analyzer = MemoryUsageAnalyzer()
    analyzer.analyze_file(filename)
