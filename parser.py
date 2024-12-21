import re
import os

class MemoryUsageParser:
    def __init__(self):
        self.malloc_pattern = re.compile(r'\bmalloc\((.*?)\)') 
        self.pointer_arithmetic_pattern = re.compile(r'\*?\((.+?)\s?\+\s?\d+\)') 
        self.memory_access_pattern = re.compile(r'\w+\[\d+\]')

    def analyze_file(self, filename):
        if not os.path.isfile(filename):  
            print(f"Error: The file '{filename}' was not found.")
            return

        with open(filename, 'r') as file:
            lines = file.readlines()

        line_number = 0
        for line in lines:
            line_number += 1
            self.check_malloc(line, line_number)
            self.check_pointer_arithmetic(line, line_number)
            self.check_memory_access(line, line_number)

    def check_malloc(self, line, line_number):
        match = self.malloc_pattern.search(line)
        if match:
            size_expression = match.group(1)
            if not re.match(r'sizeof\((\w+)\)', size_expression): 
                print(f"Line {line_number}: Potential incorrect malloc size calculation -> {line.strip()}")

    def check_pointer_arithmetic(self, line, line_number):
        match = self.pointer_arithmetic_pattern.search(line)
        if match:
            pointer_expression = match.group(1)
            print(f"Line {line_number}: Potential pointer arithmetic issue -> {line.strip()}")

    def check_memory_access(self, line, line_number):
        match = self.memory_access_pattern.search(line)
        if match:
            array_access = match.group(0)
            
            if re.search(r'\[(\d+)\]', array_access):
                index = int(re.search(r'\[(\d+)\]', array_access).group(1))
                if index < 0:
                    print(f"Line {line_number}: Off-by-one or out-of-bounds memory access -> {line.strip()}")
                elif index > 4: 
                    print(f"Line {line_number}: Off-by-one or out-of-bounds memory access -> {line.strip()}")

if __name__ == "__main__":
    filename = 'test.cpp'  
    parser = MemoryUsageParser()
    parser.analyze_file(filename)