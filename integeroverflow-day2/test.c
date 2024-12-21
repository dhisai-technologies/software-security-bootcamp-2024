#include <stdio.h>

void test_function()
{
    int x = 2147483647; // Maximum value for 32-bit int
    int y = x + 1;      // Intentional overflow
    printf("Value of y: %d\n", y);

    unsigned int z = 0;
    z = z - 1; // Intentional underflow
    printf("Value of z: %u\n", z);

    char a = 'A';
    int b = (int)a + 300; // Unsafe type casting
    printf("Value of b: %d\n", b);
}

int main()
{
    test_function();
    return 0;
}