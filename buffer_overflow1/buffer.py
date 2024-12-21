import re


def detect_vulnerabilities(cpp_code):
    vulnerabilities = []

   
    negative_index_pattern = r'\[\s*(-\d+)\s*\]'  
    pointer_arithmetic_pattern = r'\*\(\s*([a-zA-Z0-9_]+)\s*[-+*/%]\s*(\d+)\s*\)'
    out_of_bounds_write_pattern = r'(\w+)\[\s*(\d+)\s*\]\s*='  
    buffer_size_pattern = r'char\s+(\w+)\s*(\d*)\['  


    cpp_code_lines = cpp_code.split('\n')

   
    buffer_sizes = {}

    
    size_matches = re.findall(buffer_size_pattern, cpp_code)
    for match in size_matches:
        buffer_name, size = match
        buffer_sizes[buffer_name] = int(size) if size else 10 

    
    for line_num, line in enumerate(cpp_code_lines, start=1):
        
        if re.search(negative_index_pattern, line):
            vulnerabilities.append(f"Vulnerability detected (Negative array index) in line {line_num}: {line.strip()}")

       
        pointer_arithmetic_match = re.search(pointer_arithmetic_pattern, line)
        if pointer_arithmetic_match:
           
            ptr_offset = int(pointer_arithmetic_match.group(2)) 
            if ptr_offset >= 0:
                vulnerabilities.append(f"Vulnerability detected (Pointer arithmetic) in line {line_num}: {line.strip()}")
            else:
                vulnerabilities.append(f"Vulnerability detected (Pointer arithmetic past buffer) in line {line_num}: {line.strip()}")

        
        match = re.search(out_of_bounds_write_pattern, line)
        if match:
            array_name = match.group(1)
            index = int(match.group(2))

    
            if array_name in buffer_sizes and index >= buffer_sizes[array_name]:
                vulnerabilities.append(f"Vulnerability detected (Out-of-bounds write) in line {line_num}: {line.strip()}")

   
    vulnerabilities = list(set(vulnerabilities))

    return vulnerabilities


def read_cpp_code_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading the file: {e}")
        return ""

if __name__ == "__main__":
    
    cpp_file_path = 'vulnerable_code.cpp'  

    
    cpp_code = read_cpp_code_from_file(cpp_file_path)

    
    if cpp_code:
        vulnerabilities = detect_vulnerabilities(cpp_code)

        
        if vulnerabilities:
            print("\nDetected vulnerabilities:")
            for vuln in vulnerabilities:
                print(vuln)
        else:
            print("\nNo vulnerabilities detected.")
    else:
        print("\nFailed to read C++ code. Please check the file path.")
