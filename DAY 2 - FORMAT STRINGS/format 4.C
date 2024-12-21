#include <stdio.h>

void vulnerable_sprintf(char *user_input) {
    char buffer[100];
    sprintf(buffer, user_input); // Vulnerable: directly using user-controlled input
}
