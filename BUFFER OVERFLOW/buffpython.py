def detect_buffer_overrun_vulnerabilities(cpp_code):
    vulnerabilities = []
    unsafe_functions = ['strcpy', 'strcat', 'sprintf', 'gets', 'scanf']
    for func in unsafe_functions:
        if func in cpp_code:
            vulnerabilities.append(f"Unsafe function '{func}' detected. This can lead to buffer overrun.")
    if 'new' in cpp_code and '[' in cpp_code and ']' in cpp_code:
        if 'delete' in cpp_code or '=' in cpp_code:
            vulnerabilities.append("Dynamic array allocation detected without bounds checking. This can lead to buffer overrun.")
    if 'char' in cpp_code and '[' in cpp_code and ']' in cpp_code:
        vulnerabilities.append("Raw array declaration detected without bounds checking. This can lead to buffer overrun.")

    if '*' in cpp_code and '+' in cpp_code or '-' in cpp_code:
        vulnerabilities.append("Unsafe pointer arithmetic detected. This can lead to memory corruption or buffer overrun.")

    if not vulnerabilities:
        vulnerabilities.append("No buffer overrun vulnerabilities detected.")

    return vulnerabilities


filename = input("Please enter the path to the C++ file: ")
try:
    with open(filename, 'r') as file:
        cpp_code = file.read()
        vulnerabilities = detect_buffer_overrun_vulnerabilities(cpp_code)
        for vuln in vulnerabilities:
            print(vuln)
    
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")