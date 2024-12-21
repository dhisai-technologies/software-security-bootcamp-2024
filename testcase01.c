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

