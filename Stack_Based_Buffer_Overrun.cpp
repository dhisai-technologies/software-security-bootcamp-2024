void stack_example() {
    char buffer[50];        // Fixed size buffer on stack
    strcpy(buffer, "Overflow this!");  // Unsafe strcpy
    gets(buffer);           // Unsafe gets
}
END
