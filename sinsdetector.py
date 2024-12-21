import re

# Define a regular expression pattern to match format string functions
format_string_functions = r'\b(?:printf|sprintf|fprintf|snprintf|vsprintf|vsnprintf)\b'

# Define a regular expression pattern to detect unsafe use cases
unsafe_patterns = r'%.*[^%]*\((.*)\)|[^%]*\b(?:stdin|gets|fgets|scanf|strtok|malloc|realloc)\b.*\)'

# A regex pattern to detect explicit fixed format strings (like "%s")
fixed_format_strings = r'"%[^"]+"'

def detect_format_string_vulnerability(file_content):
    """
    Detects potential format string vulnerabilities in the given C code.
    Args:
        file_content (str): The content of the C source code file to analyze.
    Returns:
        List of potential vulnerabilities found.
    """
    vulnerabilities = []
    
    # Find all function calls to format string functions
    function_calls = re.finditer(format_string_functions, file_content)
    
    for match in function_calls:
        func_name = match.group(0)
        func_start = match.start()
        
        # Check if the format string is user-controlled (i.e., coming from user input)
        # This regex looks for any user-controlled input sources (e.g., stdin, fgets, etc.)
        unsafe_usage = re.search(unsafe_patterns, file_content[func_start:])
        
        # Avoid flagging the code as vulnerable if the format string is a fixed one
        # Example: snprintf(buffer, sizeof(buffer), "%s", user_input);
        fixed_format = re.search(fixed_format_strings, file_content[func_start:])
        
        if unsafe_usage and not fixed_format:
            # Flag this function call as a potential vulnerability
            vulnerabilities.append({
                'function': func_name,
                'location': func_start,
                'unsafe_input': unsafe_usage.group(1)
            })
    
    return vulnerabilities

def scan_code(file_content):
    """
    Scans a C source code for format string vulnerabilities.
    Args:
        file_content (str): The content of the C source code to analyze.
    """
    # Detect vulnerabilities
    vulnerabilities = detect_format_string_vulnerability(file_content)
    
    if vulnerabilities:
        print("Potential vulnerabilities found in the provided C code:")
        for vuln in vulnerabilities:
            print(f"Function {vuln['function']} at position {vuln['location']} "
                  f"may use unsafe input: {vuln['unsafe_input']}")
    else:
        print("No vulnerabilities found in the provided C code.")

if __name__ == "__main__":
    # Example C code to analyze (you can replace this with your own code)
    test_case_1 = """
    #include <stdio.h>

    void vulnerable_function(char *user_input) {
        printf(user_input);  // Vulnerability: format string takes user input
    }

    int main() {
        char buffer[100];
        fgets(buffer, 100, stdin);  // User input is fetched
        vulnerable_function(buffer);  // User input passed directly to printf
        return 0;
    }
    """
    
    test_case_2 = """
    #include <stdio.h>

    void secure_function(char *user_input) {
        snprintf(user_input, 100, "%s", user_input);  // Safe: format string is fixed
        printf("%s", user_input);  // Output is safe
    }

    int main() {
        char buffer[100];
        fgets(buffer, 100, stdin);  // User input is fetched
        secure_function(buffer);    // User input passed safely to snprintf
        return 0;
    }
    """
    
    # Scan the first test case (vulnerable)
    print("Scanning Test Case 1 (Vulnerable):")
    scan_code(test_case_1)
    print("\n" + "="*50 + "\n")
    
    # Scan the second test case (secure)
    print("Scanning Test Case 2 (Secure):")
    scan_code(test_case_2)



