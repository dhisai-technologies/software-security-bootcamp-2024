#include <iostream>
#include <cstring>

void vulnerableFunction(const char* input) {
    char buffer[10];
    char* ptr = buffer - 5;  // Pointer before the beginning of the buffer
    strcpy(ptr, input);      // Writing to memory outside the bounds of the buffer
    std::cout << "Buffer content: " << buffer << std::endl;
}

int main() {
    const char* dangerousInput = "This is too long!";
    vulnerableFunction(dangerousInput);
    return 0;
}
