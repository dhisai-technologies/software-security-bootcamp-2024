import re

def detect_integer_overflow(code):
    """
    Detects potential integer overflow vulnerabilities in C/C++ code.

    Args:
        code: The C/C++ code string.

    Returns:
        A list of potential integer overflow vulnerabilities.
    """

    vulnerabilities = []

    # Regular expressions to identify potential overflow scenarios
    overflow_patterns = [
        # Addition
        r"(\w+)\s*=\s*(\w+)\s*\+\s*(\w+)",
        # Subtraction
        r"(\w+)\s*=\s*(\w+)\s*\-\s*(\w+)",
        # Multiplication
        r"(\w+)\s*=\s*(\w+)\s*\*\s*(\w+)",
        # Division
        r"(\w+)\s*=\s*(\w+)\s*\/\s*(\w+)",
        # Bitwise operators
        r"(\w+)\s*=\s*(\w+)\s*(\&|\||\^)\s*(\w+)",
        # Shifts
        r"(\w+)\s*=\s*(\w+)\s*(<<|>>)\s*(\w+)",
    ]

    for pattern in overflow_patterns:
        for match in re.finditer(pattern, code):
            var1 = match.group(1)
            var2 = match.group(2)
            var3 = match.group(3)
            operator = match.group(4) if len(match.groups()) > 3 else None

            # Check for potential overflow based on variable types and operator
            # (This is a simplified check, more sophisticated analysis is required)
            if any(t in ["char", "short", "int"] 
                    for t in [get_variable_type(var1, code), 
                             get_variable_type(var2, code), 
                             get_variable_type(var3, code)]):
                vulnerabilities.append(
                    f"Potential integer overflow: {match.group(0)}"
                )

    return vulnerabilities

def get_variable_type(variable, code):
    """
    Extracts the declared type of a variable from the code.

    Args:
        variable: The name of the variable.
        code: The C/C++ code string.

    Returns:
        The declared type of the variable (e.g., "int", "char", "unsigned int").
    """
    # This is a simplified implementation, more robust parsing is needed
    pattern = r"(\w+)\s*" + variable 
    match = re.search(pattern, code)
    if match:
        return match.group(1)
    return None

# Example usage
code = """
int main() {
    int a = 10;
    int b = 20;
    int c = a + b; 

    char d = 127;
    d = d + 1; // Potential overflow

    return 0;
}
"""

vulnerabilities = detect_integer_overflow(code)
for vuln in vulnerabilities:
    print(vuln)
