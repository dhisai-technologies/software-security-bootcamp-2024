import sys
import re

# Function to detect signed integer overflow
def detect_signed_overflow(line):
    # Signed integers range from -2147483648 to 2147483647 (32-bit example)
    signed_int_min = -2147483648
    signed_int_max = 2147483647

    # Regular expression to match arithmetic operations involving integers
    pattern = r'(\d+)\s*[\+\-\*/\%]\s*(\d+)'
    matches = re.findall(pattern, line)
    
    for match in matches:
        num1, num2 = int(match[0]), int(match[1])
        
        # Check if the operation could result in an overflow (very basic detection)
        result = num1 + num2
        if result < signed_int_min or result > signed_int_max:
            return True
        
    return False

# Function to detect unsigned integer overflow
def detect_unsigned_overflow(line):
    # Unsigned integers range from 0 to 4294967295 (32-bit example)
    unsigned_int_max = 4294967295

    # Regular expression to match arithmetic operations involving integers
    pattern = r'(\d+)\s*[\+\-\*/\%]\s*(\d+)'
    matches = re.findall(pattern, line)
    
    for match in matches:
        num1, num2 = int(match[0]), int(match[1])

        # Check if the operation could result in an overflow (very basic detection)
        result = num1 + num2
        if result > unsigned_int_max:
            return True
        
    return False

# Function to detect mixed data type operations
def detect_mixed_operations(line):
    # Regular expression to detect mixed int and float operations
    pattern = r'(\d+)\s*[\+\-\*/\%]\s*(\d+\.\d+)|\s*(\d+\.\d+)\s*[\+\-\*/\%]\s*(\d+)'
    matches = re.findall(pattern, line)
    
    if matches:
        return True
    return False

# Function to analyze the C++ file
def analyze_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                # Check for integer overflows
                if detect_signed_overflow(line):
                    print(f"Potential signed integer overflow detected in line {i + 1}: {line.strip()}")
                
                if detect_unsigned_overflow(line):
                    print(f"Potential unsigned integer overflow detected in line {i + 1}: {line.strip()}")
                
                # Check for mixed data type operations
                if detect_mixed_operations(line):
                    print(f"Potential mixed data type operation detected in line {i + 1}: {line.strip()}")
                    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to take filename input from the user
def main():
    # Get the filename from the command line argument
    if len(sys.argv) < 2:
        print("Usage: python static_analysis_tool.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    analyze_file(filename)

if __name__ == '__main__':
    main()








