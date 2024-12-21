#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char buffer[256];
    printf("Enter your name: ");
    gets(buffer);

    
    printf(buffer);
    fprintf(stderr, "Error: %s\n", argv[1]); 
    printf("Hello, %s\n", buffer); 
    return 0;
}
