import re

def detect_vulnerabilities(file_path, print_all=True):
    with open(file_path, 'r') as file:
        input = file.readlines()

    # Updated regex patterns
    printf_pattern = r'\bprintf\s*\(\s*([^"%]*\w+[^"%]*)\s*\).*?(?=\s*//|$)'
    gets_pattern = r'\bgets\s*\(.*?\).*?(?=\s*//|$)'
    string_pattern = r'char\s+\w+\s*\[\s*\d*\s*\]\s*=\s*("[^"]*").*?(?=\s*//|$)'

    num = 0

    for line in input:
        # Skip lines with comments or empty lines
        if '//' in line or line.strip() == '':
            num += 1
            continue

        matches_printf = re.findall(printf_pattern, line)
        matches_gets = re.findall(gets_pattern, line)
        matches_strings = re.findall(string_pattern, line)
        num += 1

        print("\nChecking Line ", num, ":", end=" ") if print_all else None
        print(line.strip()) if print_all else None

        # Check for printf format specifiers
        for match in matches_printf:
            if not any(fmt in match for fmt in ['%s', '%x', '%p', '%d', '%f']):
                print(f'\nWARNING: printf without valid format specifier detected on line {num}')

        # Check for gets usage
        for match in matches_gets:
            print(f'\nWARNING: gets detected on line {num}, consider replacing it with fgets')

        # Check for string definitions with potential vulnerabilities
        for match in matches_strings:
            print(f'\nWARNING: String defined with potential format specifiers detected on line {num}:', match)

detect_vulnerabilities('input.c', print_all = False)