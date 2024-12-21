#include <iostream>  

int main() {
    // Test Case 1: Negative Array Index Access
    char buffer1[10];
    buffer1[-1] = 'A';  // (negative index)
    std::cout << "Buffer 1: " << buffer1 << std::endl;

    // Test Case 2: Pointer Arithmetic Writing Before Buffer
    char buffer2[10];
    char* ptr2 = &buffer2[0];
    *(ptr2 - 1) = 'B';  //(pointer arithmetic)
    std::cout << "Buffer 2: " << buffer2 << std::endl;

    // Test Case 3: Incorrect Loop Index Writing Before the Buffer
    char buffer3[10];
    for (int i = -1; i < 9; ++i) {
        buffer3[i] = 'C';  //  (incorrect index)
    }
    std::cout << "Buffer 3: " << buffer3 << std::endl;

    // Test Case 4: Out of bounds write (index 10 for array of size 10)
    char buffer4[10];
    buffer4[10] = 'D';  // out of bound
    std::cout << "Buffer 4: " << buffer4 << std::endl;

    // Test Case 5: Writing Past the End Using Pointer Arithmetic
    char buffer5[10];
    char* ptr5 = &buffer5[9];
    *(ptr5 + 1) = 'E';  //  past the end of the buffer
    std::cout << "Buffer 5: " << buffer5 << std::endl;

    return 0;
}
