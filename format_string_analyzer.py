import re
code=input('enter the code:')
def detect_vulnerabilities(code):
    vulnerabilities = []
    codej = 'System.out.printf'

    # Detect unsafe printf patterns
    patternc = r'printf\s*\(([^)]*)\)'
    patternj=r'System.out.printf\s*\(([^)]*)\)'
    
    if codej in code:
        pattern = patternj

    else:
        pattern = patternc

    matches = re.findall(pattern, code)


    for match in matches:
        if '%n' in match:
            vulnerabilities.append("Warning: Use of %n detected.")
        if '%x' in match:
            vulnerabilities.append("Warning: Use of %x detected.")
        if '%p' in match:
            vulnerabilities.append("Warning: Use of %p detected.")
    

    vul1 = 'printf(user_input);' #vulnerable code for c
    vul2 = 'System.out.printf(userInput);' #vulnerable code for java

    if vul1 in code:
        print('Dangerous if `input` is user-controlled!!->',code)
        print('Safer Alternative: printf("%s", user_input)')
    elif vul2 in code:
        print('Dangerous if `input` is user-controlled!!->',code)
        print('Safer Alternative: System.out.printf("%s", userInput);')

    return vulnerabilities
print(detect_vulnerabilities(code))
