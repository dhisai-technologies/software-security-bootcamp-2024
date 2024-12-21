#include <stdio.h>

int main() {
    // Addition (Potential Overflow)
    int result_add = 2147483647 + 1;
    printf("Addition Result: %d\n", result_add); 

    // Subtraction (Potential Underflow)
    int result_sub = -2147483648 - 1;
    printf("Subtraction Result: %d\n", result_sub);

    // Division (Division by Zero)
    int a = 10;
    int result_div = a / 0;
    printf("Division Result: %d\n", result_div); 

    // Multiplication (Potential Overflow)
    int result_mul = 1073741824 * 2;
    printf("Multiplication Result: %d\n", result_mul);

    // Bit-Shift (Potential Unsafe Right Shift)
    int x = 1;
    int result_right_shift = x >> 30;
    printf("Right Shift Result: %d\n", result_right_shift);

    // Bit-Shift (Potential Unsafe Left Shift)
    int y = 1;
    int result_left_shift = y << 30;  
    printf("Left Shift Result: %d\n", result_left_shift);

    // Safe Bit Shift
    int z = 8;
    int result_safe_shift = z << 2;  
    printf("Safe Shift Result: %d\n", result_safe_shift); 

    return 0;
}