#include <iostream>
#include <climits>

int main() {
    // Test Case 1: Integer Overflow
    int x1 = INT_MAX;
    int result1 = x1 + 1; // Integer overflow
    std::cout << "Test Case 1 - Integer Overflow: " << result1 << std::endl;

    // Test Case 2: Integer Overflow with Subtraction
    int x2 = INT_MIN;
    int result2 = x2 - 1; // Integer overflow
    std::cout << "Test Case 2 - Integer Overflow with Subtraction: " << result2 << std::endl;

    // Test Case 3: Unsigned Integer Overflow
    unsigned int x3 = UINT_MAX;
    unsigned int result3 = x3 + 1; // Unsigned integer overflow
    std::cout << "Test Case 3 - Unsigned Integer Overflow: " << result3 << std::endl;

    // Test Case 4: Buffer Overflow
    char buffer1[5];
    buffer1[5] = 'A';
    std::cout << "Test Case 4 - Buffer Overflow: Completed" << std::endl;

    // Test Case 5: Buffer Overflow with Function
    char buffer2[5];
    auto writeBuffer = [&]() {
        for (int i = 0; i < 10; i++) { // Buffer overflow
            buffer2[i] = 'B';
        }
    };
    writeBuffer();
    std::cout << "Test Case 5 - Buffer Overflow with Function: Completed" << std::endl;

    // Test Case 6: Division by Zero
    int y1 = 10;
    int z1 = y1 / 0; // Division by zero
    std::cout << "Test Case 6 - Division by Zero: " << z1 << std::endl;

    // Test Case 7: Division by Zero with Variable
    int y2 = 0;
    int z2 = 10 / y2; // Division by zero
    std::cout << "Test Case 7 - Division by Zero with Variable: " << z2 << std::endl;

    // Test Case 8: Division by Zero with Conditional
    int y3 = 0;
    if (y3 == 0) {
        std::cout << "Test Case 8 - Division by Zero avoided with Conditional Check." << std::endl;
    } else {
        int z3 = 10 / y3;
        std::cout << "Test Case 8 - Division by Zero: " << z3 << std::endl;
    }

    // Test Case 9: Dynamic Buffer Overflow
    int size = 5;
    char *buffer3 = new char[size];
    for (int i = 0; i <= size; i++) { // Dynamic buffer overflow
        buffer3[i] = 'C';
    }
    delete[] buffer3;
    std::cout << "Test Case 9 - Dynamic Buffer Overflow: Completed" << std::endl;

    // Test Case 10: Integer Overflow in Loop
    int x4 = INT_MAX - 1;
    for (int i = 0; i < 3; i++) { // Integer overflow in loop
        x4 += 1;
    }
    std::cout << "Test Case 10 - Integer Overflow in Loop: " << x4 << std::endl;

    return 0;
}
