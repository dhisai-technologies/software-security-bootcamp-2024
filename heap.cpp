#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *vulnerable_heap_function(char *input) {
    char *buffer = (char *)malloc(10);
    strcpy(buffer, input); // No bounds checking
    return buffer;
}

int main() {
    char malicious_input[20] = "AAAAAAAAAAAAAAAAAAAA";
    char *ptr = vulnerable_heap_function(malicious_input);
    free(ptr); // Potential memory corruption if buffer overflowed
    return 0;
}