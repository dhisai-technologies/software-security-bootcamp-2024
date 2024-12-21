import re

def detect_vulnerability(code):
    vulnerability = []

    
    pattern = r'printf\s*\(([^)]*)\)'
    matches = re.findall(pattern, code)

    for match in matches:
        if '%n' in match:
            vulnerability.append("Warning: %n is used.")
        if '%x' in match:
            vulnerability.append("Warning: %x is used.")
        if '%p' in match:
            vulnerability.append("Warning: %p is used.")
    return vulnerability


def main():
    test_file = 'test_cases.txt'

    try:
        with open(test_file, 'r') as file:
            test_cases = file.readlines()

        if not test_cases:
            print("Error: The test cases file is empty.")
            return

        print("=== Format String Vulnerability Analysis ===\n")
        
        for i, test_case in enumerate(test_cases, 1):
            test_case = test_case.strip()
            if not test_case:  
                print(f"Test Case {i}: Skipped (empty line)\n")
                continue
            
            print(f"Test Case {i}: {test_case}")
            
            vulnerability = detect_vulnerability(test_case)
            
            if vulnerability:
                for warning in vulnerability:
                    print(f"  {warning}")
            else:
                print("  No vulnerabilities detected.")
            print()
    
    except FileNotFoundError:
        print(f"Error: The file '{test_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
