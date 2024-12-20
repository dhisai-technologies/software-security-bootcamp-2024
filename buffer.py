import re

def detect_buffer_overrun_vulnerabilities(cpp_code):
    vulnerabilities = []

    
    patterns = {
        "Unsafe string functions": [r'\bstrcpy\s*\(', r'\bstrcat\s*\(', r'\bgets\s*\(', r'\bsprintf\s*\('],
        "Unbounded loop (<=)": [r'for\s*\(.*\s*i\s*=\s*.*;\s*i\s*<=\s*.*;\s*i\+\+\)'],
        "Array access without bounds check": [r'\[\s*\]', r'(\w+)\s*\[\s*(\w+)\s*\]']
    }

    
    for vulnerability, pattern_list in patterns.items():
        for pattern in pattern_list:
            if re.search(pattern, cpp_code):
                vulnerabilities.append(vulnerability)

    return vulnerabilities



cpp_code = '''
void vulnerable_function(char* input) {
    char buffer[64];
    strcpy(buffer, input);  // No size checking!
    printf("Input: %s\\n", buffer);
}

void another_vulnerable_function(int* data, int size) {
    int array[5];
    for(int i = 0; i <= size; i++) {  // Potential overflow
        array[i] = data[i];
    }
}

int main(int argc, char *argv[]) {
    char buffer[50];
    strcpy(buffer, argv[1]);  // No validation!
    return 0;
}
'''

vulnerabilities = detect_buffer_overrun_vulnerabilities(cpp_code)


if vulnerabilities:
    print("Vulnerabilities detected:")
    for vulnerability in vulnerabilities:
        print(vulnerability)
else:
    print("No vulnerabilities detected.")
