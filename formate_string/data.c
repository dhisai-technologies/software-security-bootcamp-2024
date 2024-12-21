#include <stdio.h>

int main() {
    char input[100];
    scanf("%s", input);
    printf(input); // Unsafe
    printf("%s", input); // Safe
    return 0;
}
