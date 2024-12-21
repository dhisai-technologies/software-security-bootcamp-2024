#include <cstring>
void unsafeFunction(const char* input) {
    char output[10];
    strcpy(output, input); // Unsafe: No size check
    strncpy(output, input, 20); // Unsafe: Size exceeds buffer
    strncpy(output, input, sizeof(output) - 1); // Safe usage
}
