<<<<<<< HEAD
import re

def detect_vulnerabilities(filename):
    with open(filename, 'r') as f:
        code = f.read()

    #
    patterns = [
        r'strcpy\([^,]+, .+\)',
        r'strcat\([^,]+, .+\)',
        r'sprintf\([^,]+, .+\)',
        r'gets\(.+\)',
        r'\[[^\]]+\]\s*=\s*.+\s*\[[^\]]+\]',  
        r'for\s*\([^;]+;\s*[^;]+[<>=!]+\s*[^;]+;\s*[^;]+\)',  
    ]

    print(f"Checking {filename} for vulnerabilities...\n")
    for pattern in patterns:
        matches = re.findall(pattern, code)
        if matches:
            print(f"Potential vulnerabilities found using pattern '{pattern}':")
            for match in matches:
                print(f"- {match}")


filename = 'stack.cpp'
detect_vulnerabilities(filename)
=======
import re

def detect_vulnerabilities(filename):
    with open(filename, 'r') as f:
        code = f.read()

    #
    patterns = [
        r'strcpy\([^,]+, .+\)',
        r'strcat\([^,]+, .+\)',
        r'sprintf\([^,]+, .+\)',
        r'gets\(.+\)',
        r'\[[^\]]+\]\s*=\s*.+\s*\[[^\]]+\]',  
        r'for\s*\([^;]+;\s*[^;]+[<>=!]+\s*[^;]+;\s*[^;]+\)',  
    ]

    print(f"Checking {filename} for vulnerabilities...\n")
    for pattern in patterns:
        matches = re.findall(pattern, code)
        if matches:
            print(f"Potential vulnerabilities found using pattern '{pattern}':")
            for match in matches:
                print(f"- {match}")


filename = 'stack.cpp'
detect_vulnerabilities(filename)
>>>>>>> 64eae8323ed0fb129b1170d6253d2ea1dff9c058
