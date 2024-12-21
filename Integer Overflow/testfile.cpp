#include <iostream>
using namespace std;
int main() {
    unsigned int x = -10; // Potential underflow
    int y = 2147483647;
    y += 1; // Potential overflow
    double z = 5.5;
    int w = (int)z; // Unsafe type casting
    return 0;