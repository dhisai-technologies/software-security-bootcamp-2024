import re

def analyze_code(code):
    errors = []
    
    # Detect malloc() calls and check size calculation
    malloc_pattern = r"malloc\s*\(([^)]+)\)"
    for match in re.finditer(malloc_pattern, code):
        malloc_expr = match.group(1)
        if not re.match(r"sizeof\s*\(.+\)\s*(\*|\/|\+|-)?\s*\d*", malloc_expr):
            errors.append(f"Potential incorrect size calculation in malloc(): {malloc_expr}")

    # Detect pointer arithmetic
    pointer_arith_pattern = r"(\w+)\s*=\s*\w+\s*\+\s*(\w+|\d+)"
    for match in re.finditer(pointer_arith_pattern, code):
        pointer = match.group(1)
        offset = match.group(2)
        if not re.match(r"\w+\s*<\s*\w+", offset):
            errors.append(f"Pointer arithmetic without bound check: {pointer} = ... + {offset}")
    
    # Detect off-by-one errors in memory access
    access_pattern = r"(\w+)\[(.+)\]"
    for match in re.finditer(access_pattern, code):
        array = match.group(1)
        index = match.group(2)
        if re.search(r"length|size", index, re.IGNORECASE) and not re.search(r"-\s*1", index):
            errors.append(f"Potential off-by-one error in memory access: {array}[{index}]")

    return errors

# Test code
c_code = """
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = malloc(sizeof(int) * 10); // Correct malloc
    int *arr2 = malloc(10); // Incorrect malloc
    int *ptr = arr + 11; // Out-of-bounds pointer arithmetic
    for (int i = 0; i <= 10; i++) { // Off-by-one error
        arr[i] = i;
    }
    return 0;
}
"""

# Analyze the C code
errors = analyze_code(c_code)

# Display results
if errors:
    print("Detected Issues:")
    for error in errors:
        print(f"- {error}")
else:
    print("No issues detected.")
