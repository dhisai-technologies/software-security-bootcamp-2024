#include <iostream>

void vulnerableFunction() {
    char buffer[10];
    int index = -1; // Index set to a negative value
    buffer[index] = 'A'; // Writing before the buffer's beginning
}

void anotherVulnerableFunction() {
    char buffer[10];
    char *ptr = buffer - 1; // Pointer referencing memory before the buffer
    *ptr = 'B'; // Writing to an invalid memory location
}

int main() {
    vulnerableFunction();
    anotherVulnerableFunction();
    return 0;
}
