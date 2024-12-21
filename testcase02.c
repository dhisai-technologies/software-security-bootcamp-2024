#include <stdio.h>

void secure_function(char *user_input) {
    snprintf(user_input, 100, "%s", user_input);  // Safe: format string is fixed
    printf("%s", user_input);  // Output is safe
}

int main() {
    char buffer[100];
    fgets(buffer, 100, stdin);  // User input is fetched
    secure_function(buffer);    // User input passed safely to snprintf
    return 0;
}
