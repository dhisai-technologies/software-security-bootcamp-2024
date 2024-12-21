<<<<<<< HEAD
#include <stdio.h>
#include <stdlib.h>

int main() {
    char user_input[50];
    
    // Potentially unsanitized input
    printf("Enter your username: ");
    gets(user_input);  // Unsanitized input

    // Potentially unsanitized output
    printf("Welcome, %s!\n", user_input);  // Unsanitized output

    return 0;
}
=======
#include <stdio.h>
#include <stdlib.h>

int main() {
    char user_input[50];
    
    // Potentially unsanitized input
    printf("Enter your username: ");
    gets(user_input);  // Unsanitized input

    // Potentially unsanitized output
    printf("Welcome, %s!\n", user_input);  // Unsanitized output

    return 0;
}
>>>>>>> c63a4ae47a5b125c3334f4f068ed6897f6d6f2eb
