import re

def detect_buffer_overruns(code):
    # Patterns for stack-based buffer overflows
    stack_patterns = [
        r"char\s+\w+\[\d+\];\s*strcpy\(\w+,\s*.*?\);",  # strcpy without size check
        r"char\s+\w+\[\d+\];\s*gets\(\w+\);",           # gets used with stack buffer
    ]

    # Patterns for heap-based buffer overflows
    heap_patterns = [
        r"malloc\(\d+\);\s*gets\(\w+\);",               # malloc followed by unsafe gets
        r"malloc\(\d+\);.*strcpy\(\w+,\s*.*?\);",       # malloc with strcpy
    ]

    # Checking for stack-based buffer overruns
    print("\nChecking for Stack-Based Buffer Overruns:")
    for pattern in stack_patterns:
        matches = re.findall(pattern, code)
        if matches:
            print(f"Vulnerability Found: {pattern}")
            for match in matches:
                print(f"  -> {match}")
        else:
            print("No vulnerabilities found for this pattern.")

    # Checking for heap-based buffer overruns
    print("\nChecking for Heap-Based Buffer Overruns:")
    for pattern in heap_patterns:
        matches = re.findall(pattern, code)
        if matches:
            print(f"Vulnerability Found: {pattern}")
            for match in matches:
                print(f"  -> {match}")
        else:
            print("No vulnerabilities found for this pattern.")


# Main program
print("Enter your C++ code below:")
cpp_code = ""
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    cpp_code += line + "\n"

# Run the detection
detect_buffer_overruns(cpp_code)
