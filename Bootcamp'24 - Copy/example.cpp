#include <iostream>
#include <limits>

void demonstrateOverflow() {
    int a = 2147483640;  // Close to the maximum value of int
    int b = 10;
    int c = a + b;       // Potential overflow

    std::cout << "Sum: " << c << std::endl; // Overflow may cause undefined behavior

    int largeArray[100];
    for (int i = 0; i < 200; ++i) { // Loop exceeds array bounds
        largeArray[i % 100] = i;
    }

    int x = std::numeric_limits<int>::max();
    int y = 2;
    int result = x * y; // Multiplication overflow

    std::cout << "Result: " << result << std::endl;

    int largeValue = 1000000000;
    for (int i = 0; i < largeValue; ++i) { // Loop with a very large limit
        if (i % 100000000 == 0) {
            std::cout << "Iteration: " << i << std::endl;
        }
    }
}

int main() {
    demonstrateOverflow();
    return 0;
}
