#include <stdio.h>

void vulnerable_array_function(int *array, int size) {
    for (int i = 0; i <= size; i++) { // Potential overflow
        printf("%d\n", array[i]);
    }
}

int main() {
    int array[5] = {1, 2, 3, 4, 5};
    vulnerable_array_function(array, 5);
    return 0;
}