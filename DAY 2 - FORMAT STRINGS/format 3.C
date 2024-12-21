#include <stdio.h>

void safe_printf(char *user_input) {
    printf("%s", user_input); // Safe: explicitly specifying format string
}
