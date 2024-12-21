import re

def analyze_printf_vulnerabilities(c_code):
    printf_pattern = re.compile(r'printf\s*\(\s*["\']([^"\']+)["\']\s*,?\s*(.*?)(\);)', re.DOTALL)
    
    vulnerabilities = []
    
    # Find all printf statements in the provided C code
    matches = printf_pattern.findall(c_code)
    
    for match in matches:
        format_string = match[0]
        user_input = match[1].strip()
        
        if user_input and not re.match(r'^[\'"]', user_input):
            vulnerabilities.append({
                'format_string': format_string,
                'user_input': user_input,
                'line': c_code.count('\n', 0, c_code.index(match[0])) + 1 
            })
    
    return vulnerabilities

file = open("testcase3.txt" , "r")
content = file.read()
file.close()

vulnerabilities_found = analyze_printf_vulnerabilities(content)

if vulnerabilities_found:
    print("Potential vulnerabilities found:")
    for vuln in vulnerabilities_found:
        print(f"Line {vuln['line']}: printf with format string '{vuln['format_string']}' using user input '{vuln['user_input']}'")
else:
    print("No vulnerabilities found.")