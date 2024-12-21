import re

def parse_c_code(c_code):
    array_declaration_pattern = re.compile(r"\b(int|float|char|double)\s+([a-zA-Z_][a-zA-Z_0-9]*)\[(\d+)\]")
    array_access_pattern = re.compile(r"([a-zA-Z_][a-zA-Z_0-9]*)\[([a-zA-Z_0-9+\-*/]+)\]")
    for_loop_pattern = re.compile(r"for\s*\(([^;]+);([^;]+);([^\)]+)\)")

    arrays = {}
    for match in array_declaration_pattern.finditer(c_code):
        array_name = match.group(2)
        array_size = int(match.group(3))
        arrays[array_name] = array_size

    risks = []

    for match in array_access_pattern.finditer(c_code):
        array_name = match.group(1)
        index_expr = match.group(2)

        if array_name in arrays:
            try:
                # Evaluate the index expression (only works for constant indices)
                index_value = eval(index_expr, {"__builtins__": None}, {})
                if index_value >= arrays[array_name]:
                    risks.append(f"Out-of-bounds access: {array_name}[{index_expr}] exceeds size {arrays[array_name]}")
            except:
                # Variable index detected
                risks.append(f"Variable index access detected: {array_name}[{index_expr}] may exceed bounds {arrays[array_name]}")

    for match in for_loop_pattern.finditer(c_code):
        init, condition, increment = match.groups()
        for array_name, size in arrays.items():
            if array_name in condition:
                risks.append(f"Loop condition involving array {array_name} may exceed bounds {size}: {condition}")

    nested_array_access_pattern = re.compile(r"([a-zA-Z_][a-zA-Z_0-9]*)\[([a-zA-Z_0-9+\-*/]+)\]\[([a-zA-Z_0-9+\-*/]+)\]")
    for match in nested_array_access_pattern.finditer(c_code):
        array_name = match.group(1)
        row_index_expr = match.group(2)
        col_index_expr = match.group(3)

        if array_name in arrays:
            risks.append(f"Nested array access detected: {array_name}[{row_index_expr}][{col_index_expr}] may exceed bounds.")

    return risks

c_code = """
int arr[10];
for (int i = 0; i <= 10; i++) {
    arr[i] = i;
}
int x = 5;
arr[x + 6] = 20;
int mat[5][5];
mat[2][6] = 42;
"""

risks = parse_c_code(c_code)
if risks:
    print("Potential buffer overflow risks found:")
    for risk in risks:
        print("-", risk)
else:
    print("No potential buffer overflow risks found.")
