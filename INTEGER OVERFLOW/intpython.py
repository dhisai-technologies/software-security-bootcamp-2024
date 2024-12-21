import re
import os
from typing import List, Dict, Tuple
from dataclasses import dataclass
from enum import Enum

class VulnerabilityType(Enum):
    SIGNED_OVERFLOW = "Signed Integer Overflow"
    UNSIGNED_OVERFLOW = "Unsigned Integer Overflow"
    MIXED_TYPE = "Mixed Data Type Operation"
    TYPE_CONVERSION = "Unsafe Type Conversion"
    ARITHMETIC_OPERATION = "Unsafe Arithmetic Operation"

@dataclass
class Vulnerability:
    type: VulnerabilityType
    line_number: int
    code: str
    description: str
    severity: str
    recommendation: str

class ArithmeticVulnerabilityScanner:
    def __init__(self):
        # Patterns for detecting arithmetic vulnerabilities
        self.patterns = {
            # Signed integer overflow patterns
            'signed_overflow': [
                (r'int\s+\w+\s*=\s*(?:INT_MAX|2147483647)', 'Possible signed integer overflow with MAX value'),
                (r'int\s+\w+\s*\+\+\s*(?:\/\/.*)?$', 'Potential overflow in increment operation'),
                (r'int\s+\w+\s*\+=\s*\d+', 'Possible overflow in addition operation'),
                (r'int\s+\w+\s*\*=\s*\d+', 'Potential overflow in multiplication')
            ],
            
            # Unsigned integer overflow patterns
            'unsigned_overflow': [
                (r'unsigned\s+\w+\s*=\s*0\s*;', 'Possible unsigned underflow risk'),
                (r'unsigned\s+\w+\s*--', 'Potential unsigned underflow in decrement'),
                (r'unsigned\s+\w+\s*-=', 'Risk of unsigned underflow in subtraction')
            ],
            
            # Mixed type operation patterns
            'mixed_type': [
                (r'(int|long)\s*\w+\s*=\s*\w+\s*\+\s*(float|double)', 'Mixed integer and floating-point operation'),
                (r'(float|double)\s*\w+\s*=\s*(int|long)', 'Implicit type conversion'),
                (r'\(float\)\s*\w+', 'Explicit casting between different types')
            ],
            
            # Type conversion patterns
            'type_conversion': [
                (r'static_cast<(int|long)>\s*\((float|double)', 'Potential data loss in type conversion'),
                (r'\(int\)\s*\w+', 'Unsafe C-style type casting'),
                (r'reinterpret_cast<\w+>', 'Dangerous reinterpret_cast usage')
            ]
        }

    def scan_file(self, file_path: str) -> List[Vulnerability]:
        vulnerabilities = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                
            for line_num, line in enumerate(lines, 1):
                self._check_line_for_vulnerabilities(line, line_num, vulnerabilities)
                
            return vulnerabilities
            
        except Exception as e:
            print(f"Error scanning file: {e}")
            return []

    def _check_line_for_vulnerabilities(self, line: str, line_num: int, 
                                      vulnerabilities: List[Vulnerability]):
        for category, patterns in self.patterns.items():
            for pattern, description in patterns:
                if re.search(pattern, line):
                    vuln_type = self._get_vulnerability_type(category)
                    severity = self._get_severity(category)
                    recommendation = self._get_recommendation(category)
                    
                    vulnerabilities.append(
                        Vulnerability(
                            type=vuln_type,
                            line_number=line_num,
                            code=line.strip(),
                            description=description,
                            severity=severity,
                            recommendation=recommendation
                        )
                    )

    def _get_vulnerability_type(self, category: str) -> VulnerabilityType:
        category_map = {
            'signed_overflow': VulnerabilityType.SIGNED_OVERFLOW,
            'unsigned_overflow': VulnerabilityType.UNSIGNED_OVERFLOW,
            'mixed_type': VulnerabilityType.MIXED_TYPE,
            'type_conversion': VulnerabilityType.TYPE_CONVERSION
        }
        return category_map.get(category, VulnerabilityType.ARITHMETIC_OPERATION)

    def _get_severity(self, category: str) -> str:
        severity_map = {
            'signed_overflow': 'HIGH',
            'unsigned_overflow': 'HIGH',
            'mixed_type': 'MEDIUM',
            'type_conversion': 'MEDIUM'
        }
        return severity_map.get(category, 'LOW')

    def _get_recommendation(self, category: str) -> str:
        recommendations = {
            'signed_overflow': 'Use larger integer types or implement overflow checking',
            'unsigned_overflow': 'Add bounds checking before arithmetic operations',
            'mixed_type': 'Explicitly handle type conversions and check for data loss',
            'type_conversion': 'Use safe conversion methods with proper validation'
        }
        return recommendations.get(category, 'Review and implement proper safety checks')

def generate_report(vulnerabilities: List[Vulnerability], file_path: str) -> str:
    if not vulnerabilities:
        return f"No arithmetic vulnerabilities detected in {file_path}"

    report = f"\n=== Arithmetic Vulnerability Analysis Report ===\n"
    report += f"File: {file_path}\n\n"

    # Group by severity
    severity_groups = {"HIGH": [], "MEDIUM": [], "LOW": []}
    for vuln in vulnerabilities:
        severity_groups[vuln.severity].append(vuln)

    # Generate report for each severity level
    for severity in ["HIGH", "MEDIUM", "LOW"]:
        if severity_groups[severity]:
            report += f"\n{severity} Risk Vulnerabilities:\n"
            report += "=" * 50 + "\n"
            
            for vuln in severity_groups[severity]:
                report += f"\nLine {vuln.line_number}:\n"
                report += f"Type: {vuln.type.value}\n"
                report += f"Code: {vuln.code}\n"
                report += f"Description: {vuln.description}\n"
                report += f"Recommendation: {vuln.recommendation}\n"
                report += "-" * 50 + "\n"

    return report

def main():
    print("Arithmetic Vulnerability Scanner")
    print("=" * 30)

    # Get input file from user
    while True:
        file_path = input("\nEnter the path to the source code file: ").strip()
        if os.path.exists(file_path):
            break
        print("Error: File not found. Please try again.")

    scanner = ArithmeticVulnerabilityScanner()
    print("\nScanning file for arithmetic vulnerabilities...")
    
    vulnerabilities = scanner.scan_file(file_path)
    report = generate_report(vulnerabilities, file_path)
    print(report)

    # Print statistics
    if vulnerabilities:
        print(f"\n=== Vulnerability Statistics ===")
        vuln_types = {}
        severity_count = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
        
        for vuln in vulnerabilities:
            vuln_types[vuln.type.value] = vuln_types.get(vuln.type.value, 0) + 1
            severity_count[vuln.severity] = severity_count[vuln.severity] + 1

        print("\nVulnerabilities by type:")
        for vtype, count in vuln_types.items():
            print(f"{vtype}: {count}")

        print("\nVulnerabilities by severity:")
        for severity, count in severity_count.items():
            print(f"{severity}: {count}")

if __name__ == "__main__":
    main()
