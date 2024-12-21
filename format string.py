import re

def detect_vulnerabilities():
    
    try:
        with open("/home/Intelligent_Systems_Design_Lab/software-security-bootcamp-2024/day2/vuln_c_code.txt", 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print("file not found.")
        return


    pattern = r'printf\s*\(([^)]*)\)'
    matches = re.findall(pattern, code)
    
  
    vulnerable = False
    
    for match in matches:
        if '%n' in match:
            print("use of %n detected.")
            vulnerable = True
        if '%x' in match:
            print("use of %x detected.")
            vulnerable = True
        if '%p' in match:
            print("ue of %p detected.")
            vulnerable = True
    
    if not vulnerable:
        print("no vulnerable detected.")


detect_vulnerabilities()