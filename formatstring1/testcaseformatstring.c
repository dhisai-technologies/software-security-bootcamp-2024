#include <stdio.h>
#include <string.h>

void test_vulnerable_printf(char* user_input) {
    // Vulnerable usage of printf with user-controlled input
    printf(user_input);  // Unsafe
}

int main() {
    char user_input[100];
    printf("Enter input: ");
    fgets(user_input, sizeof(user_input), stdin);
    test_vulnerable_printf(user_input);
    return 0;
}
