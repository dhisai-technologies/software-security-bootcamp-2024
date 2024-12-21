def parse_code(code):
    allocations = []  # Track memory allocations
    errors = []

    for line in code.splitlines():
        # Detect memory allocation (malloc, calloc, etc.)
        if 'malloc' in line or 'calloc' in line:
            size = extract_malloc_size(line)
            allocations.append(size)

        # Detect pointer arithmetic (e.g., buf[i], arr[j])
        if 'ptr[' in line or 'ptr++' in line:
            ptr_access = extract_pointer_access(line)
            for alloc_size in allocations:
                if ptr_access > alloc_size:
                    errors.append(f"Pointer access exceeds allocated size: {line}")

        # Detect loops and array access
        if 'for' in line:
            loop_condition = extract_loop_condition(line)
            array_size = extract_array_size(line)
            if loop_condition >= array_size:
                errors.append(f"Off-by-one error in loop condition: {line}")

    return errors

# Example functions to extract sizes or conditions
def extract_malloc_size(line):
    # Extract the size argument in malloc
    pass

def extract_pointer_access(line):
    # Calculate the memory accessed by pointer
    pass

def extract_loop_condition(line):
    # Extract the loop condition
    pass

def extract_array_size(line):
    # Extract the size of an array
    pass