#include <iostream>

int main() {
    signed int a = INT_MAX; // Maximum value for signed int
    a = a + 1; // Overflow
    std::cout << a << std::endl;
    return 0;
}
