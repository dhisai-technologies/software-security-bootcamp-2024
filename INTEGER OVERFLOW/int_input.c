#include <stdio.h>
#include <string.h>

int main() {
    // Signed integer overflow
    int x = 2147483647;  // Max value for a 32-bit signed integer
    int y = 1;
    x = x + y;  // This might cause an overflow

    // Unsigned integer underflow
    unsigned int u = 0;
    u = u - 1;  // This will cause an underflow since u is unsigned

    // Mixed data type operation
    int a = 5;
    float b = 10.5;
    int result = a + b;  // Implicit conversion from float to int might cause loss of precision

    // Unsafe function usage
    gets(x);  // Unsafe 'gets' function
    scanf("%d", &x);  // No input validation for scanf

    // Unsafe type casting
    float f = 10.5;
    int i = (int)f;  // Unsafe type casting (loss of precision)
    
    // Format string vulnerability
    printf("%s", x);  // Potential format string vulnerability

    // Improper exception handling
    try {
        printf("This is a try block without a catch.\n");
    }  // Missing catch block

    // Unsafe string copying
    char dest[10];
    strcpy(dest, "This is a very long string that will overflow.");

    return 0;
}
