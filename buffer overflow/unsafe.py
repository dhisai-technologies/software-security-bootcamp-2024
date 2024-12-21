from pycparser import c_parser, c_ast
import os

class UnsafeStringUsageChecker(c_ast.NodeVisitor):
    """
    A visitor class to check for unsafe string operations in C code.
    """
    UNSAFE_FUNCTIONS = {'strcpy', 'strcat', 'gets'}

    def __init__(self):
        self.issues = []

    def visit_FuncCall(self, node):
        """
        Visit function call nodes to check for unsafe string operations.
        """
        if isinstance(node.name, c_ast.ID) and node.name.name in self.UNSAFE_FUNCTIONS:
            issue = {
                "function": node.name.name,
                "line": node.coord.line,
                "context": node.show()
            }
            # Check for buffer size verification
            if node.name.name in {'strcpy', 'strcat'}:
                if not self.is_safe_operation(node):
                    self.issues.append(issue)
            elif node.name.name == 'gets':  # 'gets' is inherently unsafe
                self.issues.append(issue)

        self.generic_visit(node)

    def is_safe_operation(self, node):
        """
        Placeholder for checking if an operation is safe (e.g., bounds-checked).
        In a real implementation, this would analyze preceding logic for buffer size checks.
        """
        # Advanced logic could analyze the code for checks like strlen, sizeof, etc.
        return False

def analyze_code(source_code):
    """
    Parse and analyze the C source code for unsafe string operations.
    """
    parser = c_parser.CParser()
    try:
        ast = parser.parse(source_code)
    except Exception as e:
        print("Parsing failed:", e)
        return []

    checker = UnsafeStringUsageChecker()
    checker.visit(ast)
    return checker.issues

if __name__ == "__main__":
    # File path to analyze
    source_file = r"C:\Users\moksh\OneDrive\Desktop\python 1\test.py"  # Raw string to handle backslashes

    if not os.path.isfile(source_file):
        print(f"Error: The file '{source_file}' does not exist. Please provide a valid file path.")
    else:
        try:
            with open(source_file, "r") as file:
                source_code = file.read()

            # Analyze the source code
            issues = analyze_code(source_code)
            if issues:
                print("Unsafe string function usage detected:")
                for issue in issues:
                    print(f"Function '{issue['function']}' at line {issue['line']}")
                    print(f"Context:\n{issue['context']}")
            else:
                print("No unsafe string function usage detected.")
        except Exception as e:
            print(f"An error occurred while processing the file: {e}")
