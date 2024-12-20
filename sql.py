import ast

class SQLInjectionDetector(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    def visit_Call(self, node):
        """Inspect function calls for unsafe string formatting."""
        if isinstance(node.func, ast.Name) and node.func.id.lower() in ['execute', 'executemany']:
            
            for arg in node.args:
                if isinstance(arg, ast.JoinedStr):  
                    self.issues.append((node.lineno, "f-strings in queries"))
                elif isinstance(arg, ast.BinOp) and isinstance(arg.op, ast.Mod):
                    self.issues.append((node.lineno, "%-formatting in SQL queries"))
        self.generic_visit(node)

    def visit_Assign(self, node):
        """Inspect assignments for unsafe string concatenation."""
        if isinstance(node.value, ast.BinOp) and isinstance(node.value.op, ast.Mod):
            self.issues.append((node.lineno, "%-formatting in SQL queries"))
        if isinstance(node.value, ast.JoinedStr):
            self.issues.append((node.lineno, "f-strings in queries"))
        self.generic_visit(node)

    def visit_Expr(self, node):
        """Inspect expressions for unsafe string concatenation."""
        if isinstance(node.value, ast.BinOp) and isinstance(node.value.op, ast.Mod):
            self.issues.append((node.lineno, "%-formatting in SQL queries"))
        if isinstance(node.value, ast.JoinedStr):
            self.issues.append((node.lineno, "f-strings in queries"))
        self.generic_visit(node)

    def report_issues(self):
        if not self.issues:
            print("No issues detected.")
        else:
            print("Potential SQL Injection Risks Detected:")
            for lineno, message in self.issues:
                print(f"Line {lineno}: {message}")


if __name__ == "__main__":
    code = """
username = "user"
query = f"SELECT * FROM users WHERE username = '{username}'"
cursor.execute(query)
query2 = "SELECT * FROM users WHERE username = %s" % username
cursor.execute(query2)
"""
    tree = ast.parse(code)
    detector = SQLInjectionDetector()
    detector.visit(tree)
    detector.report_issues()
