

#include <stdio.h>
#include <string.h>

void host_lookup(char *user_supplied_addr) {
    struct hostent *hp;
    in_addr_t *addr;
    char hostname[64];
    in_addr_t inet_addr(const char *cp);
    
    // Routine that ensures user_supplied_addr is in the right format for conversion
    validate_addr_form(user_supplied_addr);
    addr = inet_addr(user_supplied_addr);
    hp = gethostbyaddr(addr, sizeof(struct in_addr), AF_INET);
    
    // Vulnerable code: unsafe function usage (strcpy)
    strcpy(hostname, hp->h_name);
}

int main() {
    char user_addr[] = "127.0.0.1";
    host_lookup(user_addr);
    return 0;
}