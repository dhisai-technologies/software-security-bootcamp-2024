#include <stdio.h>

int main() {
    char name[50];
    int age;

    // Example of using gets (unsafe)
    printf("Enter your name: ");
    gets(name);

    // Valid printf
    printf("Hello, %s!\n", name);
    
    // Invalid printf (no valid format specifier)
    printf(name);

    //Invalid 
    char input[] = "%x %n %p";
    printf(input);

    // Another valid printf
    printf("You are %d years old.\n", age);

    // Another invalid printf (no valid format specifier)
    printf(name);

    return 0;
}
