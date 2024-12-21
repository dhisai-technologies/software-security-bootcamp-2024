import re


patterns = {
    'addition': re.compile(r'(\w+)\s*\+\s*(\w+)'),  
    'multiplication': re.compile(r'(\w+)\s*\*\s*(\w+)'),  
    'casting': re.compile(r'\(\s*(\w+)\s*\)\s*(\w+)'),  
}


def detect_integer_overflow(file_path):
    vulnerabilities = []
    
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        
        for line_number, line in enumerate(lines, start=1):
            
            if patterns['addition'].search(line):
                vulnerabilities.append({
                    'line': line_number,
                    'type': 'Addition',
                    'code': line.strip(),
                    'description': f"Potential integer overflow in addition operation on line {line_number}.",
                })
            
            if patterns['multiplication'].search(line):
                vulnerabilities.append({
                    'line': line_number,
                    'type': 'Multiplication',
                    'code': line.strip(),
                    'description': f"Potential integer overflow in multiplication operation on line {line_number}.",
                })
          
            if patterns['casting'].search(line):
                vulnerabilities.append({
                    'line': line_number,
                    'type': 'Casting',
                    'code': line.strip(),
                    'description': f"Potential integer overflow in type casting on line {line_number}.",
                })
        
    except Exception as e:
        print(f"Error: {e}")
    
    return vulnerabilities


def analyze_file(file_path):
    print(f"Analyzing file: {file_path}\n")
    vulnerabilities = detect_integer_overflow(file_path)
    
    if vulnerabilities:
        print("Potential vulnerabilities detected:\n")
        for vuln in vulnerabilities:
            print(f"Line {vuln['line']}: {vuln['description']}")
            print(f"    Code: {vuln['code']}\n")
    else:
        print("No integer overflow vulnerabilities detected.")


c_code = """
#include <stdio.h>

int main() {
    int transaction_amount = 1000000000;  
    int fraud_threshold = 2000000000;     
    int risk_score = 100;                 
    int risk_multiplier = 50;             
    int final_risk_score;
    
    if (transaction_amount + fraud_threshold > 10000000000) {  
    
        
        final_risk_score = risk_score * risk_multiplier;  
        
  
        short small_risk_score = (short)final_risk_score;  
        
       
        final_risk_score = final_risk_score + risk_score;  
    }
    
    return 0;
}
"""

file_name = "fraud_detection_vulnerable_example.c"
with open(file_name, "w") as file:
    file.write(c_code)
print(f"Step 1: New C code with fraud detection details and integer overflow vulnerabilities has been saved to {file_name}")


analyze_file(file_name)
