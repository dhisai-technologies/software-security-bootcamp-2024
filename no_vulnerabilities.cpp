void safe_example() {
    char buffer[64];
    strncpy(buffer, "Safe input", sizeof(buffer) - 1);  // Safe strncpy
    buffer[sizeof(buffer) - 1] = '\0';                 // Null-terminate
}
END
