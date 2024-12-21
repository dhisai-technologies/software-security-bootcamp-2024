#include <stdlib.h>
#include <stdio.h>

void testMemory()
{
    int *arr = (int *)malloc(5 * sizeof(int));
    if (!arr)
    {
        fprintf(stderr, "Error: Memory allocation for arr failed\n");
        return;
    }

    for (int i = 0; i < 5; i++)
    {
        arr[i] = i + 1; // Assigning values within bounds
    }

    int outOfBoundsValue = 20;
    printf("Attempting out-of-bounds access with value %d\n", outOfBoundsValue);

    int *another_arr = (int *)calloc(10, sizeof(int));
    if (!another_arr)
    {
        fprintf(stderr, "Error: Memory allocation for another_arr failed\n");
        free(arr);
        return;
    }

    for (int i = 0; i < 10; i++)
    {
        another_arr[i] = (i + 1) * 2; // Initialize values within bounds
    }

    free(arr);
    free(another_arr);
}

void anotherFunction()
{
    char *str = (char *)malloc(20 * sizeof(char));
    if (!str)
    {
        fprintf(stderr, "Error: Memory allocation for str failed\n");
        return;
    }

    for (int i = 0; i < 20; i++)
    {
        str[i] = 'A' + (i % 26); // Safely assigning within bounds
    }
    str[19] = '\0'; // Null-terminate the string

    printf("Generated string: %s\n", str);

    free(str);
}

int main()
{
    testMemory();
    anotherFunction();
    return 0;
}
