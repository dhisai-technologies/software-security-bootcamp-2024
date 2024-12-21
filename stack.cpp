#include <stdio.h>
#include <string.h>

void vulnerable_function(char *input) {
    char buffer[10];
    strcpy(buffer, input); // No bounds checking
    printf("Input: %s\n", buffer);
}

int main() {
    char malicious_input[20] = "AAAAAAAAAAAAAAAAAAAA";
    vulnerable_function(malicious_input);
    return 0;
}