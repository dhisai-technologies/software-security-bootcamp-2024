import re

def detect_buffer_overflow(file_path):
    try:
        with open(file_path, 'r') as file:
            cpp_code = file.read()  # Read the C++ code from the file
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    except Exception as e:
        print(f"Error reading the file: {e}")
        return

    # Regular expression patterns to detect buffer overflow/underflow
    overflow_pattern = re.compile(r'buffer\[\d+\]')
    underflow_pattern = re.compile(r'buffer\[-\d+\]')
    buffer_size = 10  # Assuming a buffer size of 10

    # Detect overflow
    overflow_matches = re.findall(overflow_pattern, cpp_code)
    if overflow_matches:
        for match in overflow_matches:
            index_match = re.search(r'\d+', match)
            if index_match:
                index = int(index_match.group())
                if index >= 10 and index <0:  # Flag out-of-bounds indices
                    print(f"Buffer access out of bounds detected: {match}")

    # Detect underflow
    underflow_matches = re.findall(underflow_pattern, cpp_code)
    if underflow_matches:
        for match in underflow_matches:
            print(f"Buffer underflow detected: {match}")

    if not (overflow_matches or underflow_matches):
        print("No buffer overflow/underflow detected.")

# Main entry point
file_path = 'buffer 2.txt'
detect_buffer_overflow(file_path)
