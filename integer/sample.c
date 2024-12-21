#include <limits.h>
#include <string.h>
#include <stdio.h>

void test() {
    int a = 2147483647; // Possible integer overflow
    char buffer[10];    // Buffer overflow potential
    int b = 10, c = 0;
    int result = b / c; // Division by zero
}
