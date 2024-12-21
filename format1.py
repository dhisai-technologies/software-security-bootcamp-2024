import os
import re
import argparse


def find_potentially_unsanitized_code(file_path):
    with open(file_path, 'r',encoding = 'utf-8',errors='ignore') as file:
        code = file.readlines()
    suspicious_lines = []

    output_functions = re.compiler(r'\b(?:printf|sprintf|fprintf|std::cout|std::snprintf)\b')

    input_functions = re.compile(r'\b(? : scanf|fgets|getchar|gets|std::cin)\b')

    for i, line in enumerate(code, start=1):
        if input_functions.search(line):
           
            for j in range(i + 1, min(i + 5, len(code))): 
                if output_functions.search(code[j]):
                    suspicious_lines.append((i, line.strip()))
                    break

                if output_functions.search(line) and any(var in line for var in ["%s", "%d", "%f", "%lf"]):
                               suspicious_lines.append((i, line.strip()))   

    return suspicious_lines
def analyze_directory(directory):
    results = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.c', '.cpp')):
                file_path = os.path.join(root, file)
                suspicious_lines = find_potentially_unsanitized_code(file_path)

                if suspicious_lines:
                    results[file_path] = suspicious_lines

    return results

def main():
    parser = argparse.ArgumentParser(description="Analyze C and C++ code for unsanitized user input.")
    parser.add_argument("directory", help="Path to the directory containing C/C++ source files")
    args = parser.parse_args()

    results = analyze_directory(args.directory)

    if results:
        print("Potentially unsanitized input found:")
        for file_path, issues in results.items():
            print(f"\nIn file: {file_path}")
            for line_no, line in issues:
                print(f"  Line {line_no}: {line}")
    else:
        print("No potentially unsanitized input found.")

if __name__ == "__main__":
    main()



