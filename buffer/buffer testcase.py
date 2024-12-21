import re

def detect_unsafe_usage(code):
    unsafe_functions = ['strcpy', 'strcat', 'gets', 'sprintf']
    warnings = []


    for function in unsafe_functions:
        if re.search(r'\b' + function + r'\s*\(.*\)\s*;', code):
            warnings.append(f"Unsafe function call detected: {function}()")

    return warnings

code = """
    char buffer[100];
    strcpy(buffer, "Safe");
    strcat(buffer, " Functions");
    strcpy_s(buffer, 100, "Safe Usage");
    gets(buffer);
    sprintf(buffer, "Unsafe");
"""

warnings = detect_unsafe_usage(code)


for warning in warnings:
    print(warning)

