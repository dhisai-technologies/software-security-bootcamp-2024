import re

# Function to detect buffer overflow vulnerabilities
def detect_buffer_overflow(c_code):
    vulnerabilities = []

    # Check for the use of strcpy without length checks
    if re.search(r'\bstrcpy\(', c_code):
        vulnerabilities.append("Potential buffer overflow due to unsafe use of strcpy.")

    # Check if a fixed-size buffer is being copied into without bounds checking
    buffer_match = re.search(r'char\s+(\w+)\[\d+\];', c_code)
    if buffer_match:
        buffer_name = buffer_match.group(1)
        # Check for strcpy using this buffer without checking the length
        if re.search(rf'\bstrcpy\({buffer_name},', c_code):
            vulnerabilities.append(f"Potential buffer overflow when copying into buffer {buffer_name}.")

    # Check for unvalidated string inputs (i.e., user-supplied addresses)
    if re.search(r'validate_addr_form\(', c_code) is None:
        vulnerabilities.append("Unvalidated user input (user_supplied_addr).")

    return vulnerabilities

# Example C code to analyze
c_code = """
void host_lookup(char *user_supplied_addr){
    struct hostent *hp;
    in_addr_t *addr;
    char hostname[64];
    in_addr_t inet_addr(const char *cp);
    
    /* routine that ensures user_supplied_addr is in the right format for conversion */
    validate_addr_form(user_supplied_addr);
    addr = inet_addr(user_supplied_addr);
    hp = gethostbyaddr(addr, sizeof(struct in_addr), AF_INET);
    strcpy(hostname, hp->h_name);
}
"""

# Detect vulnerabilities in the given C code
vulnerabilities = detect_buffer_overflow(c_code)

# Print detected vulnerabilities
if vulnerabilities:
    print("Detected Vulnerabilities:")
    for vulnerability in vulnerabilities:
        print(f"- {vulnerability}")
else:
    print("No vulnerabilities detected.")
