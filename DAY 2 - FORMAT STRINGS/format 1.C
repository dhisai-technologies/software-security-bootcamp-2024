#include <stdio.h>

void vulnerable_function(char *user_input) {
    printf(user_input);  // Vulnerable format string
}
