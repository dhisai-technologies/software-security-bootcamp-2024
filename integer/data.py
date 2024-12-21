import re
import os

def detect_vulnerabilities(file_path):
    """
    Detect vulnerabilities in the given C/C++ file.
    :param file_path: Path to the C/C++ file.
    :return: Dictionary of detected vulnerabilities.
    """
    vulnerabilities = {
        "Integer Overflow": [],
        "Buffer Overflow": [],
        "Division by Zero": [],
    }

    try:
        with open(file_path, "r") as file:
            code = file.read()

            # Detect Integer Overflow
            int_overflow_pattern = r"(\w+\s*=\s*\w+\s*\+\s*\d+;)"
            vulnerabilities["Integer Overflow"] = re.findall(int_overflow_pattern, code)

            # Detect Buffer Overflow
            buffer_overflow_pattern = r"(char\s+\w+\[\d+\];)"
            vulnerabilities["Buffer Overflow"] = re.findall(buffer_overflow_pattern, code)

            # Detect Division by Zero
            division_by_zero_pattern = r"(\w+\s*=\s*\w+\s*/\s*\w+;)"
            vulnerabilities["Division by Zero"] = re.findall(division_by_zero_pattern, code)

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return vulnerabilities


def generate_test_cases(vulnerabilities, file_language="C"):
    """
    Generate test cases for the detected vulnerabilities.
    :param vulnerabilities: Dictionary of vulnerabilities.
    :param file_language: Language of the input file ("C" or "C++").
    :return: String of test cases.
    """
    test_cases = []

    if vulnerabilities["Integer Overflow"]:
        for vuln in vulnerabilities["Integer Overflow"]:
            variable = re.search(r"(\w+)\s*=", vuln).group(1)
            test_cases.append(
                f"// Test case for Integer Overflow\n"
                f"{variable} = INT_MAX; // Assign maximum integer value\n"
                f"{vuln.replace(variable, variable + ' + 1')}\n"
                f"// Expected: Overflow\n"
            )

    if vulnerabilities["Buffer Overflow"]:
        for vuln in vulnerabilities["Buffer Overflow"]:
            variable = re.search(r"char\s+(\w+)\[", vuln).group(1)
            test_cases.append(
                f"// Test case for Buffer Overflow\n"
                f"{vuln}\n"
                f"strcpy({variable}, \"This input is way too long for the buffer\");\n"
                f"// Expected: Overflow\n"
            )

    if vulnerabilities["Division by Zero"]:
        for vuln in vulnerabilities["Division by Zero"]:
            numerator, denominator = re.search(r"(\w+)\s*/\s*(\w+);", vuln).groups()
            test_cases.append(
                f"// Test case for Division by Zero\n"
                f"int {denominator} = 0;\n"
                f"{vuln}\n"
                f"// Expected: Division by zero error\n"
            )

    return "\n".join(test_cases)


def main():
    # Ask the user for the input file path
    input_file = input("Enter the path to the C/C++ file: ").strip()

    # Validate file existence
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    # Detect vulnerabilities
    vulnerabilities = detect_vulnerabilities(input_file)

    # Print detected vulnerabilities
    print("Detected Vulnerabilities:")
    for vuln_type, instances in vulnerabilities.items():
        if instances:
            print(f"\n{vuln_type}:")
            for instance in instances:
                print(f"- {instance}")
        else:
            print(f"\n{vuln_type}: None detected.")

    # Generate and print test cases
    print("\nGenerated Test Cases:")
    test_cases = generate_test_cases(vulnerabilities)
    print(test_cases if test_cases else "No test cases generated.")


if __name__ == "__main__":
    main()
