#include <iostream>
#include <climits>

int main() {
    int a = INT_MAX;
    int b = a + 1;  // Potential overflow
    unsigned int c = 0;
    c = c - 1;  // Potential underflow
    int d = 100;
    d = d * a;  // Potential overflow

    return 0;
}
