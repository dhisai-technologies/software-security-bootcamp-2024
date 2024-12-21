def unsafe_strcpy(dest, src):
    """
    Simulates the unsafe strcpy function in Python.
    Overwrites the destination with the source.
    """
    log_unsafe_usage("strcpy")
    return src

def unsafe_strcat(dest, src):
    """
    Simulates the unsafe strcat function in Python.
    Concatenates the source to the destination without bounds checking.
    """
    log_unsafe_usage("strcat")
    return dest + src

def unsafe_gets():
    """
    Simulates the unsafe gets function in Python.
    Reads input from the user without any length validation.
    """
    log_unsafe_usage("gets")
    return input("Enter a string (no bounds checking): ")

# Simulating a database to store unsafe usage logs
unsafe_usage_database = []

def log_unsafe_usage(function_name):
    """
    Logs the usage of unsafe string functions to the database.
    """
    unsafe_usage_database.append({
        "function": function_name,
        "message": f"Unsafe usage detected: {function_name} called without bounds checking."
    })

def test_function():
    buffer = " " * 10  # Mimic a buffer with a fixed size of 10 characters
    input_data = "This is unsafe!"
    
    print("Initial buffer:", repr(buffer))
    
    # Simulate strcpy
    print("\nUsing unsafe_strcpy:")
    buffer = unsafe_strcpy(buffer, input_data)
    print("Buffer after unsafe_strcpy:", repr(buffer))

    # Simulate strcat
    print("\nUsing unsafe_strcat:")
    buffer = unsafe_strcat(buffer, input_data)
    print("Buffer after unsafe_strcat:", repr(buffer))

    # Simulate gets
    print("\nUsing unsafe_gets:")
    buffer = unsafe_gets()
    print("Buffer after unsafe_gets:", repr(buffer))

def display_unsafe_usage():
    """
    Display the unsafe string function usage logs.
    """
    if unsafe_usage_database:
        print("\n--- Unsafe String Function Usage Detected ---")
        for log in unsafe_usage_database:
            print(f"Function: {log['function']} - {log['message']}")
    else:
        print("\nNo unsafe string function usage detected.")

if __name__ == "__main__":
    test_function()
    display_unsafe_usage()
