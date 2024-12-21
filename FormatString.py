import re

def detect_user_input_in_templates(file_content, language):
    if language not in ["C", "C++"]:
        print(f"Language {language} not supported.")
        return

    patterns = {
        "C": [
            r'printf\s*\(\s*".*%\w.*",\s*[^\)]+\s*\)',  
            r'sprintf\s*\(.*\s*,\s*".*%\w.*",\s*[^\)]+\s*\)',  
        ],
        "C++": [
            r'cout\s*<<\s*.*\s*<<\s*[^\s;]+',  
            r'format\s*\(\s*".*%\w.*",\s*[^\)]+\s*\)',  
        ]
    }

    for pattern in patterns[language]:
        if re.search(pattern, file_content):
            print(f"Potential user-generated input in templates detected in {language} code!\nPattern: {pattern}")
        else:
            print(f"No vulnerability detected in {language} code for pattern:\n{pattern}")



file_path = 'FormatString.c' 
with open(file_path, 'r') as file:
    file_content = file.read()

detect_user_input_in_templates(file_content, "C") 
