import re

# Define regex patterns to detect potential vulnerabilities
patterns = {
    "integer_overflow_addition": r"(\d+|\w+)\s*\+\s*(\d+|\w+)",
    "integer_overflow_multiplication": r"(\d+|\w+)\s*\*\s*(\d+|\w+)",
    "integer_overflow_shift": r"(\w+)\s*<<\s*(\d+|\w+)|\s*>>\s*(\d+|\w+)",
    "pointer_arithmetic": r"\*(\w+)\s*[\+\-\*/]\s*(\d+|\w+)",
    "unsafe_pointer_dereference": r"\*\s*(\w+)\s*=\s*[^;]+",
    "array_size_issue": r"new\s+(\w+)\s*\[\s*(\d+|\w+)\s*\]",
    "array_out_of_bounds": r"\[\d+\]",
}

def check_for_overflows_and_issues(code):
    issues = []
    
    if re.search(patterns["integer_overflow_addition"], code):
        issues.append("Potential integer overflow in addition.")
    else:
        print("no error in addition")
    
    if re.search(patterns["integer_overflow_multiplication"], code):
        issues.append("Potential integer overflow in multiplication.")
    else:
        print("no error in multiplication")
    
    if re.search(patterns["integer_overflow_shift"], code):
        issues.append("Potential integer overflow in shift operations.")
    else:
        print("no error in bitwise shifts")
    
    if re.search(patterns["pointer_arithmetic"], code):
        issues.append("Potential unsafe pointer arithmetic.")
    else:
        print("no error in pointer arithmetic (out-of-bounds)")
    
    if re.search(patterns["unsafe_pointer_dereference"], code):
        issues.append("Potential unsafe pointer dereference.")
    else:
        print("no error in pointer dereference")
    
    if re.search(patterns["array_size_issue"], code):
        issues.append("Potential issue with array size allocation.")
    else:
        print("no error in array size allocation")
    
    if re.search(patterns["array_out_of_bounds"], code):
        issues.append("Potential array index out of bounds.")
    else:
        print("no error in array access (potential out-of-bounds access)")
    
    return issues

def analyze_cpp_file(filename):
    try:
        with open(filename, 'r') as file:
            code = file.read()
        
        issues = check_for_overflows_and_issues(code)
        
        if issues:
            print(f"Issues found in {filename}:")
            for issue in issues:
                print(f" - {issue}")
        else:
            print(f"No issues found in {filename}.")
    
    except Exception as e:
        print(f"Error reading file {filename}: {e}")

if __name__ == "__main__":
    cpp_file = r'C:\PERSONAL\test_case-3.txt'  # Update with the correct path to your C++ file
    analyze_cpp_file(cpp_file)
