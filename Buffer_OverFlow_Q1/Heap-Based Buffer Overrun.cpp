void heap_example() {
    char* buf = (char*)malloc(20);  // Heap allocation
    gets(buf);                      // Unsafe gets
    strcpy(buf, "Unsafe strcpy!");  // Unsafe strcpy
    free(buf);
}
END
