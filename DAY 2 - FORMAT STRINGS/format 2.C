#include <stdio.h>

void vulnerable_printf(char *user_input) {
    printf(user_input); // Vulnerable: directly using user-controlled input
}
