#include <iostream>
using namespace std;

int main() {
    // Example of Addition Overflow
    int a = 2147483647; // Max value for 32-bit signed int
    int b = 1;
    int result = a + b; // Potential overflow

    // Example of Subtraction Underflow
    unsigned int c = 0;
    unsigned int d = 1;
    unsigned int underflow_result = c - d; // Potential underflow

    // Example of Division by Zero
    int numerator = 10;
    int denominator = 0;
    int division_result = numerator / denominator; // Division by zero

    // Example of Bitwise Operations
    int x = 5;
    int y = 3;
    int bitwise_and = x & y; // Bitwise AND operation

    // Example of Shifts
    int shift_left = x << 31; // Potential undefined behavior due to overflow

    // Example of Multiplication Overflow
    int large_num = 1000000;
    int multiplication_result = large_num * large_num; // Potential overflow

    cout << "Example program completed." << endl;
    return 0;
}
