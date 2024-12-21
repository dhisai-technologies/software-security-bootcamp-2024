
#include <stdio.h>

int main() {
    char buffer[100];
    char *user_input = gets(buffer);
    printf(user_input); // Vulnerable
    return 0;
}
