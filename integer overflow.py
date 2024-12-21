import re

overflow_patterns = [
    r'(\w+)\s*\+\s*(\w+)',  
    r'(\w+)\s*-\s*(\w+)',  
    r'(\w+)\s*\*\s*(\w+)',  
    r'(\w+)\s*(<<|>>)\s*(\d+)', 
]

int_type_patterns = r'\b(int|long|short|unsigned\s+int|unsigned\s+long|signed\s+int|unsigned\s+short)\b'

def detect_overflows_and_types(code: str):
    """
    detect potential integer overflow vulnerabilities in C/C++ code.
    Checks for integer type declarations and overflow-prone operations.
    """
    warnings = []

    types_detected = re.findall(int_type_patterns, code)
    if types_detected:
        warnings.append(f"detected integer types: {', '.join(set(types_detected))}")
    
    for pattern in overflow_patterns:
        matches = re.findall(pattern, code)

        for match in matches:
            operation = ' '.join(match)
            warning = f"potential overflow vulnerability detected: {operation}"
            warnings.append(warning)

    if not warnings:
        return "no potential overflows detected."
    
    return '\n'.join(warnings)

c_code = """
#include <stdio.h>

int main() {
    int a = 2147483647;  // Max value for 32-bit signed integer
    int b = 1;
    int result;

    result = a + b;  // Potential overflow

    result = a - b;  // Potential overflow

    result = a * b;  // Potential overflow

    result = a << 1;  // Potential overflow

    return 0;
}
"""

overflow_warnings = detect_overflows_and_types(c_code)

print(overflow_warnings)
