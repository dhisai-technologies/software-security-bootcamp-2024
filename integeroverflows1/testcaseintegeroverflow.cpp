#include <iostream>
#include <limits>

int main() {
    int x = INT_MAX;
    x = x + 1; // Potential overflow
    x = x - 1; // Safe
    x = x * 2; // Potential overflow
    x = x / 2; // Safe
    x = x & 1; // Safe
    x = x | 1; // Safe
    x = x ^ 1; // Safe
    x = x << 1; // Potential overflow
    x = x >> 1; // Safe
    return 0;
}