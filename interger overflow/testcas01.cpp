#include <iostream>
#include <limits.h>

int main() {
    int a = INT_MAX;  // Maximum value of int
    int b = 1;
    int result = a + b;  // This will cause overflow
    std::cout << "Result: " << result << std::endl;
    return 0;
}
