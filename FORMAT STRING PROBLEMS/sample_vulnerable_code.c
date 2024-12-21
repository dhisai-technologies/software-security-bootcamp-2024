#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void vulnerable_function() {
    char buffer[100];

    // Unsafe input function: 'gets' (can cause buffer overflow)
    gets(buffer); 

    // Format string vulnerability: printf with unvalidated user input
    printf(buffer); // Vulnerability: No format specifier

    // Unsafe string copy: 'strcpy' without bounds checking
    char another_buffer[50];
    strcpy(another_buffer, buffer); // Vulnerability: No bounds checking
}

int main() {
    // Unsafe type casting: mismatched types in malloc allocation
    double* unsafe_cast = (double*)malloc(sizeof(int)); // Vulnerability: Mismatched type

    if (!unsafe_cast) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Improper exception handling: Try without catch (C doesn't support try-catch)
    try {
        throw 20; // Vulnerability: No catch block, C doesn't support try-catch
    } catch (int e) {
        printf("Exception caught: %d\n", e);
    }

    free(unsafe_cast);
    return 0;
}
