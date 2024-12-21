#include <iostream>
#include <cstring>

void exampleFunction() {
    char buffer[10];
    strcpy(buffer, "This is a very long string");
}

void unsafeArray() {
    int* arr = new int[10];
    arr[10] = 5; // No bounds checking
}

void unsafePointerArithmetic() {
    int* ptr = new int[5];
    ptr = ptr + 2;  // Unsafe pointer arithmetic
}

int main() {
    exampleFunction();
    unsafeArray();
    unsafePointerArithmetic();
    return 0;
}