#include <stdio.h>

int main() {
    unsigned int a = -1; // Potential underflow
    int b = 2147483647;
    b = b + 1; // Potential overflow
    float c = 3.5;
    int d = (int)c; // Unsafe type casting
    return 0;
}
