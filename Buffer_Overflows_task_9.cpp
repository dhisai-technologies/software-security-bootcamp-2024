//question==============
//Create a parser that analyzes command-line argument handling, it should focus on:
//
// argv[] access bounds
//String operations on arguments
//Array operations using argc
//
//#program===================
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to check bounds of argv[] access
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to check bounds of argv[] access
void check_argv_bounds(int argc, char *argv[]) {
    printf("Checking argv[] access bounds:\n");

    // Loop through the arguments and print each one
    for (int i = 0; i < argc; i++) {
        printf("Argument %d: %s\n", i, argv[i]);
    }
    printf("\n");
}

// Function to perform safe string operations on arguments
void string_operations(int argc, char *argv[]) {
    if (argc < 2) {
        printf("No arguments passed for string operations.\n\n");
        return;
    }

    // Example: Concatenate the arguments starting from argv[1]
    char concatenated[256] = "";
    for (int i = 1; i < argc; i++) {  // Start from 1 to skip the program name
        strncat(concatenated, argv[i], sizeof(concatenated) - strlen(concatenated) - 1);
        if (i < argc - 1) {
            strncat(concatenated, " ", sizeof(concatenated) - strlen(concatenated) - 1); // Add space between arguments
        }
    }
    printf("Concatenated Arguments: %s\n", concatenated);

    // Example: Calculate the length of each argument
    printf("\nArgument Lengths:\n");
    for (int i = 1; i < argc; i++) {
        printf("Length of argument %d (%s): %zu\n", i, argv[i], strlen(argv[i]));
    }
    printf("\n");
}

// Function to perform array operations using argc
void array_operations(int argc, char *argv[]) {
    printf("Performing array operations using argc:\n");

    // Print the number of arguments
    printf("Number of arguments: %d\n", argc);

    // Safely access the first and last argument
    if (argc > 1) {
        printf("First argument (argv[1]): %s\n", argv[1]);
        printf("Last argument (argv[%d]): %s\n", argc - 1, argv[argc - 1]);
    } else {
        printf("No arguments passed beyond the program name.\n");
    }

    // Example: Reverse and print arguments using argc
    printf("\nReversed Arguments:\n");
    for (int i = argc - 1; i > 0; i--) {  // Start from argc-1 to skip the program name
        printf("%s ", argv[i]);
    }
    printf("\n\n");
}

int main(int argc, char *argv[]) {
    printf("Program started with %d arguments:\n", argc);

    // Print the arguments (this includes the program name at index 0)
    for (int i = 0; i < argc; i++) {
        printf("argv[%d]: %s\n", i, argv[i]);
    }
    printf("\n");

    // Check argv[] bounds access
    check_argv_bounds(argc, argv);

    // Perform string operations
    string_operations(argc, argv);

    // Perform array operations using argc
    array_operations(argc, argv);

    return 0;
}


//Output============
//Program started with 4 arguments:
//argv[0]: ./arg_parser
//argv[1]: Hello
//argv[2]: World
//argv[3]: 123
//
//Checking argv[] access bounds:
//Argument 0: ./arg_parser
//Argument 1: Hello
//Argument 2: World
//Argument 3: 123
//
//Performing string operations using arguments:
//Concatenated Arguments: Hello World 123
//
//Argument Lengths:
//Length of argument 1 (Hello): 5
//Length of argument 2 (World): 5
//Length of argument 3 (123): 3
//
//Performing array operations using argc:
//Number of arguments: 4
//First argument (argv[1]): Hello
//Last argument (argv[3]): 123
//
//Reversed Arguments:
//123 World Hello


