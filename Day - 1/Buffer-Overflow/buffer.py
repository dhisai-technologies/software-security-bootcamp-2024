import sys

def print_usage(prog_name):
    print(f"Usage: {prog_name} [options]")
    print("Options:")
    print("  --help            Show help information")
    print("  -v                Enable verbose mode")
    print("  --count <value>   Set a count value")
    print("  <other arguments> Can be any other arguments")

def parse_arguments():
    if len(sys.argv) < 2:
        print("Error: No arguments provided.")
        print_usage(sys.argv[0])
        return

    verbose_mode = False
    count_value = None

    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]

        if arg == "--help":
            print_usage(sys.argv[0])
            return

        elif arg == "-v":
            verbose_mode = True
            print("Verbose mode enabled.")

        elif arg == "--count":
            if i + 1 < len(sys.argv):
                try:
                    count_value = int(sys.argv[i + 1])
                    print(f"Count value set to: {count_value}")
                    i += 1  # Skip the next argument, as it's already used
                except ValueError:
                    print("Error: Invalid value for --count. Please provide a valid integer.")
                    return
            else:
                print("Error: Missing value for --count")
                return

        elif arg.startswith("--"):
            print(f"Error: Unrecognized option: {arg}")
            return

        else:
            print(f"General argument {i}: {arg}")

def main():
    parse_arguments()

if __name__ == "_main_":
    main()