#include <stdio.h>
#include <string.h>

void vulnerable_function(char *user_input) {
    
    printf(user_input);
}

int main() {
    char input[100];
    printf("Enter some text: ");
    fgets(input, sizeof(input), stdin);
    

    input[strcspn(input, "\n")] = 0;

    vulnerable_function(input);
    return 0;
}
