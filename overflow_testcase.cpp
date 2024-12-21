#include <iostream>

int main() {
    int a = 2147483647; // Maximum value for a signed 32-bit integer
    int b = 1;
    int result = a + b;  // This will cause signed integer overflow
    std::cout << "Overflow result: " << result << std::endl;
    unsigned int a = 4294967295; // Maximum value for an unsigned 32-bit integer
    unsigned int b = 1;
    unsigned int result = a + b;  // This will cause unsigned integer overflow
    std::cout << "Overflow result: " << result << std::endl;
    int a = 10;
    float b = 2.5;
    float result = a + b;  // This will mix int and float types
    std::cout << "Mixed type result: " << result << std::endl;
    return 0;
}

