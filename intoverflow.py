import re
import os
from typing import List, Dict, Tuple

class ArithmeticVulnerabilityAnalyzer:
    def __init__(self):
        self.patterns = {
            'integer_overflow': [
               
                r'(\b(?:int|long|short)\b\s+\w+\s*=\s*\w+\s*\*\s*\w+)',
               
                r'(\b(?:int|long|short)\b\s+\w+\s*=\s*\w+\s*\+\s*\w+)',

                r'(\w+\+\+|\+\+\w+|\w+\s*\+=\s*\d+)',
            ],
            'integer_underflow': [
             
                r'(\b(?:unsigned\s+)?(?:int|long|short)\b\s+\w+\s*=\s*\w+\s*\-\s*\w+)',
           
                r'(\w+\-\-|\-\-\w+|\w+\s*\-=\s*\d+)',
            ],
            'type_conversion': [
               
                r'(\b(?:int|long|short)\b\s+\w+\s*=\s*\b(?:float|double)\b)',
               
                r'(\(\s*(?:int|long|short)\s*\)\s*\w+)',
              
                r'(\b(?:long|short)\b\s+\w+\s*=\s*\b(?:int|long|short)\b)',
            ],
            'division': [
              
                r'(\w+\s*\/\s*\w+)',
              
                r'(\w+\s*%\s*\w+)',
            ]
        }

    def analyze_file(self, file_path: str) -> List[Dict]:
        """
        Analyze a C++ file for potential arithmetic vulnerabilities
        """
        vulnerabilities = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                lines = content.split('\n')
                
               
                for line_num, line in enumerate(lines, 1):
                    line = line.strip()
                   
                    if not line or line.startswith('//') or line.startswith('/*'):
                        continue

                    for vuln_type, patterns in self.patterns.items():
                        for pattern in patterns:
                            matches = re.finditer(pattern, line)
                            for match in matches:
                            
                                context = self.get_context(lines, line_num - 1)
                                
                                vulnerability = {
                                    'type': vuln_type,
                                    'line_number': line_num,
                                    'line': line,
                                    'match': match.group(0),
                                    'context': context,
                                    'risk_level': self.assess_risk_level(vuln_type, line),
                                    'suggestion': self.get_suggestion(vuln_type, match.group(0))
                                }
                                vulnerabilities.append(vulnerability)
                                
        except Exception as e:
            print(f"Error analyzing file {file_path}: {e}")
            return []
            
        return vulnerabilities

    def get_context(self, lines: List[str], line_num: int, context_size: int = 2) -> List[str]:
        """Get surrounding lines for context"""
        start = max(0, line_num - context_size)
        end = min(len(lines), line_num + context_size + 1)
        return lines[start:end]

    def assess_risk_level(self, vuln_type: str, line: str) -> str:
        """Assess the risk level of a vulnerability"""
        if vuln_type == 'integer_overflow':
            if re.search(r'\*|\+{2}|\+=', line):
                return 'HIGH'
            return 'MEDIUM'
        elif vuln_type == 'integer_underflow':
            if 'unsigned' in line:
                return 'HIGH'
            return 'MEDIUM'
        elif vuln_type == 'type_conversion':
            if 'float' in line or 'double' in line:
                return 'HIGH'
            return 'MEDIUM'
        elif vuln_type == 'division':
            if '/' in line:
                return 'HIGH'
            return 'MEDIUM'
        return 'LOW'

    def get_suggestion(self, vuln_type: str, code_snippet: str) -> str:
        """Get suggestion for fixing the vulnerability"""
        suggestions = {
            'integer_overflow': """
                - Use larger integer types (e.g., long long)
                - Add overflow checking before operations
                - Consider using safe arithmetic functions
                - Use std::numeric_limits to check bounds
            """,
            'integer_underflow': """
                - Add underflow checking before operations
                - Consider using unsigned types where appropriate
                - Validate input values before operations
            """,
            'type_conversion': """
                - Use explicit type casting
                - Check value ranges before conversion
                - Consider using static_cast<>
                - Implement proper error handling for invalid conversions
            """,
            'division': """
                - Add checks for division by zero
                - Validate denominators before division
                - Consider using safe division functions
            """
        }
        return suggestions.get(vuln_type, "Review the code for potential issues")

def main():
    import sys


    analyzer = ArithmeticVulnerabilityAnalyzer()

   
    if len(sys.argv) < 2:
        file_path = input("Enter the path to the C++ source file: ").strip()
    else:
        file_path = sys.argv[1]

   
    file_path = file_path.strip('"\'')

   
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return
    
    if not file_path.endswith(('.cpp', '.cc', '.hpp', '.h')):
        print(f"Error: File '{file_path}' is not a C++ source file.")
        return

    
    vulnerabilities = analyzer.analyze_file(file_path)

    
    if vulnerabilities:
        print("\nPotential arithmetic vulnerabilities found:")
        for vuln in vulnerabilities:
            print("\n" + "="*80)
            print(f"Type: {vuln['type']}")
            print(f"Risk Level: {vuln['risk_level']}")
            print(f"Line {vuln['line_number']}: {vuln['line']}")
            print("\nContext:")
            for ctx_line in vuln['context']:
                print(f"    {ctx_line}")
            print("\nCode fragment:", vuln['match'])
            print("\nSuggestion:", vuln['suggestion'])
    else:
        print("\nNo arithmetic vulnerabilities detected.")

if __name__ == "__main__":
    main()
