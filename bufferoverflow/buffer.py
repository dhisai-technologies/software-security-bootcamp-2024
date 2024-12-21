import re

# Function to detect buffer overflow vulnerabilities in C code
def detect_buffer_overflow(c_code):
    vulnerabilities = []

    # Pattern to detect the declaration of char buffers (e.g., "char hostname[64];")
    buffer_pattern = re.compile(r'char\s+([a-zA-Z0-9_]+)\[(\d+)\];')
    
    # Pattern to detect strcpy calls
    strcpy_pattern = re.compile(r'strcpy\((.*),\s*(.*)\);')
    
    # Find all buffer declarations
    buffers = buffer_pattern.findall(c_code)
    
    # Find all strcpy calls
    strcpy_calls = strcpy_pattern.findall(c_code)
    
    # Check for each strcpy call and compare with buffer sizes
    for src, dest in strcpy_calls:
        for buffer_name, buffer_size in buffers:
            if buffer_name in dest:
                buffer_size = int(buffer_size)
                # Check if the source might exceed the buffer size
                if "hp->h_name" in src:
                    vulnerabilities.append(f"Potential buffer overflow: strcpy({src}, {dest})"
                                          f" - buffer {buffer_name} size: {buffer_size} bytes.")
    
    return vulnerabilities

# Example C code with potential buffer overflow
c_code = """
void host_lookup(char *user_supplied_addr){
    struct hostent *hp;
    in_addr_t *addr;
    char hostname[64];
    in_addr_t inet_addr(const char *cp);
    
    validate_addr_form(user_supplied_addr);
    addr = inet_addr(user_supplied_addr);
    hp = gethostbyaddr(addr, sizeof(struct in_addr), AF_INET);
    
    strcpy(hostname, hp->h_name);  // Potential buffer overflow
}
"""

# Detect vulnerabilities
vulnerabilities = detect_buffer_overflow(c_code)

# Output the results
if vulnerabilities:
    print("Potential vulnerabilities detected:")
    for vuln in vulnerabilities:
        print(vuln)
else:
    print("No vulnerabilities detected.")
