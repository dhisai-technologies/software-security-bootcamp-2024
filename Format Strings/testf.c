#include <stdio.h>
#include <stdlib.h>

void testPrintf(char *userInput) {
    // Vulnerable usage of printf
    printf(userInput);
}

void testSprintf(char *userInput) {
    char buffer[100];
    // Vulnerable usage of sprintf
    sprintf(buffer, userInput);
    printf("Buffer: %s\n", buffer);
}

void testFprintf(char *userInput) {
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }
    // Vulnerable usage of fprintf
    fprintf(file, userInput);
    fclose(file);
}

void testSecurePrintf(char *userInput) {
    // Safe usage of printf with format specifier
    printf("%s\n", userInput);
}

void testSecureSprintf(char *userInput) {
    char buffer[100];
    // Safe usage of sprintf with format specifier
    snprintf(buffer, sizeof(buffer), "%s", userInput);
    printf("Buffer: %s\n", buffer);
}

void testSecureFprintf(char *userInput) {
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }
    // Safe usage of fprintf with format specifier
    fprintf(file, "%s\n", userInput);
    fclose(file);
}

int main() {
    char userInput[100] = "User input goes here";  // Assume this is user input
    testPrintf(userInput);
    testSprintf(userInput);
    testFprintf(userInput);
    testSecurePrintf(userInput);
    testSecureSprintf(userInput);
    testSecureFprintf(userInput);
    return 0;
}
