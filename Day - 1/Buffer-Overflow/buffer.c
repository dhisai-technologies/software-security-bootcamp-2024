#include <stdio.h>
#include <string.h>
#include <stdlib.h>  // For strtol()


void print_usage(const char *prog_name) {
    printf("Usage: %s [options]\n", prog_name);
    printf("Options:\n");
    printf("  --help            Show help information\n");
    printf("  -v                Enable verbose mode\n");
    printf("  --count <value>   Set a count value\n");
    printf("  <other arguments> Can be any other arguments\n");
}


void parse_arguments(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Error: No arguments provided.\n");
        print_usage(argv[0]);
        return;
    }

   
    for (int i = 1; i < argc; i++) {
     
        if (strcmp(argv[i], "--help") == 0) {
            print_usage(argv[0]);
            return;
        }

      
        else if (strcmp(argv[i], "-v") == 0) {
            printf("Verbose mode enabled.\n");
        }

     
        else if (strcmp(argv[i], "--count") == 0) {
            if (i + 1 < argc) {
                char *endptr;
                long count = strtol(argv[i + 1], &endptr, 10);

               
                if (*endptr != '\0') {
                    printf("Error: Invalid value for --count. Please provide a valid integer.\n");
                    return;
                }

                printf("Count value set to: %ld\n", count);
                i++;  
            } else {
                printf("Error: Missing value for --count\n");
                return;
            }
        }

        else if (strstr(argv[i], "--") == argv[i]) {
            printf("Error: Unrecognized option: %s\n", argv[i]);
            return;
        }

        else {
            printf("General argument %d: %s\n", i, argv[i]);
        }
    }
}

int main(int argc, char *argv[]) {
    parse_arguments(argc, argv);
    return 0;
}

