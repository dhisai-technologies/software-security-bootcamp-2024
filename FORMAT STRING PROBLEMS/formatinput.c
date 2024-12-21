#include <stdio.h>
#include <stdlib.h>

void unsafe_function() {
    char buffer[100];
    printf("Enter input: ");
    fgets(buffer, sizeof(buffer), stdin); // Safe alternative to gets

    printf("%s", buffer); // Use explicit format string
}

int main() {
    int* ptr = (int*)malloc(sizeof(int));
    if (!ptr) {
        printf("Memory allocation failed\n");
        return 1;
    }
    free(ptr);

    return 0;
}

