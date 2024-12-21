import re
import os
def detection_c(code):  #function for detecting FORMAT STRING VULNERABILITY in C and C++#
    pattern = r'(printf|sprintf|fprintf)\((.*)\)'
    matches = re.findall(pattern,code)
    vulnerabilities = []
    for func, args in matches:
        if 'user_input' in args:  #checking the user controlled input#
            vulnerabilities.append((func,args))
    return vulnerabilities


def detection_java(code):  #function for detecting FORMAT STRING VULNERABILITY in JAVA#
    pattern = r'(System\.out\.printf|String\.format)\((.*)\)'
    matches = re.findall(pattern,code)
    vulnerabilities = []
    for func, args in matches:
        if 'user_input' in args:  #checking the user controlled input#
            vulnerabilities.append((func,args))
    return vulnerabilities


def alternative(vulnerabilities, language):
    suggestions = []
    for func, args in vulnerabilities:
        if language == 'C' or language == 'C++':
            suggestions.append(f"Replace {func}({args}) with {func}(\"%s\", {args})")
        elif language == 'Java':
            suggestions.append(f"Replace {func}({args}) with {func}(\"%s\", {args}) after validating user input")
        else:
            return "No vulnerabilities detected"
    return suggestions

def analyze_F(file_path, language):
    if not os.path.exists(file_path):
        return f"File not found: {file_path}"

    with open(file_path, 'r') as file:
        code = file.read()
        
    if language == 'C' or language == 'C++':
        vulnerabilities = detection_c(code)
    elif language == 'Java':
        vulnerabilities = detection_java(code)
    else:
        return "No vulnerabilities detected"

    suggestions = alternative(vulnerabilities, language)
    return suggestions

def analyze_MF(file_paths,language):
    results = {}
    for file_path in file_paths:
        results[file_path] = analyze_F(file_path, language)
    return results

file_paths_c = ["format 1.C","format 2.C","format 3.C","format 4.C"]
file_paths_java = ["format 1.java","format 2.java","format 3.java","format 4.java"]


print("C Code Analysis:")
c_results = analyze_MF(file_paths_c, 'C')
for file, result in c_results.items():
    print(f"File: {file}\nResult: {result}\n")

print("\nJava code Analysis:")
java_results = analyze_MF(file_paths_java, 'Java')
for file, result in java_results.items():
    print(f"File: {file}\nResult: {result}\n")
