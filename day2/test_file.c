// Arithmetic Issues in Array Sizes and Pointer Arithmetic
#include <iostream>
using namespace std;

int main() {
    // Array size arithmetic issues
    int size_a = 10;
    int size_b = -5; // Negative size issue
    if (size_b > 0) {
        int array1[size_b];
        cout << "Array of size " << size_b << " created." << endl;
    } else {
        cout << "Invalid array size." << endl;
    }

    int size_c = 2147483640;
    int size_d = 10;
    int total_size = size_c + size_d; // Potential overflow in array size
    if (total_size > 0) {
        cout << "Total size: " << total_size << endl;
    } else {
        cout << "Overflow in array size calculation." << endl;
    }

    // Pointer arithmetic issues
    int arr[5] = {1, 2, 3, 4, 5};
    int* ptr = arr;

    // Valid pointer arithmetic
    ptr += 2;
    cout << "Pointer value after valid increment: " << *ptr << endl;

    // Invalid pointer arithmetic (out-of-bounds)
    ptr += 10; // Pointer out-of-bounds issue
    cout << "Pointer value after invalid increment: " << *ptr << endl;

    // Arithmetic issues in pointer offset
    int offset = 2147483640;
    ptr = arr;
    ptr += offset; // Potential overflow in pointer arithmetic
    cout << "Pointer value after large offset: " << *ptr << endl;

    return 0;
}
