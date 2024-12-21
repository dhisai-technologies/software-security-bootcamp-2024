#include <stdio.h>

int main() {
    char userInput[100];
    printf("Enter your input: ");
    scanf("%s", userInput);

    printf("User input is: %s\n", userInput);

    char output[200];
    sprintf(output, "User entered: %s", userInput);
    printf("%s\n", output);

    return 0;
}
