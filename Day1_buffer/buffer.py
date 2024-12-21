import re

def detect_stack_heap_overruns(code):
    """
    Detects stack-based and heap-based buffer overruns in the given C++ code.
    
    Parameters:
        code (str): The C++ code to analyze.
    
    Returns:
        list: A list of vulnerabilities found in the code.
    """
    vulnerabilities = []

    # Pattern to detect unsafe stack-based operations
    stack_patterns = [
        r'\bchar\s+\w+\[\d+\];\s*strcpy\(',  # Fixed-size buffer with strcpy
        r'\bchar\s+\w+\[\d+\];\s*strcat\(',  # Fixed-size buffer with strcat
        r'\bchar\s+\w+\[\d+\];\s*gets\(',    # Fixed-size buffer with gets
        r'\bchar\s+\w+\[\d+\];\s*\w+\s*=\s*strncpy\(',  # Fixed-size buffer with strncpy
        r'\bint\s+\w+\[\d+\];.*\[.*\]=.*;',  # Array assignments without bounds checks
    ]

    # Pattern to detect unsafe heap-based operations
    heap_patterns = [
        r'\bchar\s*\*\s*\w+\s*=\s*\(char\s*\*\)\s*malloc\(',  # Malloc without size checks
        r'\bcalloc\(',  # Calloc usage
        r'\brealloc\(',  # Realloc usage
        r'\bgets\(',     # Gets usage in dynamic memory
        r'\bstrcpy\(',   # Strcpy usage in dynamic memory
        r'\bstrcat\(',   # Strcat usage in dynamic memory
    ]

    # Check for stack-based vulnerabilities
    for pattern in stack_patterns:
        matches = re.findall(pattern, code, re.MULTILINE)
        if matches:
            vulnerabilities.append(f"Stack-based vulnerability detected: {matches}")

    # Check for heap-based vulnerabilities
    for pattern in heap_patterns:
        matches = re.findall(pattern, code, re.MULTILINE)
        if matches:
            vulnerabilities.append(f"Heap-based vulnerability detected: {matches}")

    return vulnerabilities


# Example C++ Code
cpp_code = """
void vulnerable_function(char* input) {
    char buffer[64];
    strcpy(buffer, input);  // No size checking!
    printf("Input: %s\\n", buffer);
}

char* vulnerable_heap() {
    char* buf = (char*)malloc(10);
    gets(buf);  // Can read more than 10 bytes!
    return buf;
}
"""

# Run the detector
vulns = detect_stack_heap_overruns(cpp_code)

# Output results
for vuln in vulns:
    print(vuln)
