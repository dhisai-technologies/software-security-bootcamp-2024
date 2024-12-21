
#include <stdio.h>

int main() {
    char buffer[100];
    char *user_input = gets(buffer);
    printf(user_input); 
    sprintf(buffer, user_input); 
    scanf(user_input); 
    return 0;
}
