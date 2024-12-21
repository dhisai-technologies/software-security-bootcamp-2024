// test.cpp
#include <iostream>

int main() {
    // Signed integer overflow risks
    int max_value = 2147483647;
    max_value++;  // Overflow

    // Unsigned integer underflow risks
    unsigned int min_value = 0;
    min_value--;  // Underflow

    // Mixed type operations
    float pi = 3.14159;
    int rounded = pi;  // Implicit conversion

    // Unsafe type conversions
    double large_num = 1234567.89;
    int converted = (int)large_num;  // C-style cast

    // Arithmetic operations
    int result = max_value * 2;  // Overflow risk

    return 0;
}