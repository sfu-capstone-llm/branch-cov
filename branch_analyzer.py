import ast

class BranchAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.branches = []

    def visit_If(self, node):
        """Detect if-elif-else branches"""
        test_code = ast.dump(node.test) if node.test else "No condition"
        self.branches.append(f"IF: {test_code}")
        self.generic_visit(node)

        for elif_node in node.orelse:
            if isinstance(elif_node, ast.If):
                test_code = ast.dump(elif_node.test)
                self.branches.append(f"ELIF: {test_code}")
                self.generic_visit(elif_node)
            elif elif_node:
                self.branches.append("ELSE")
                self.generic_visit(elif_node)

    def visit_For(self, node):
        """Detect for loops"""
        self.branches.append(f"FOR: iterating {ast.dump(node.target)}")
        self.generic_visit(node)

    def visit_While(self, node):
        """Detect while loops"""
        self.branches.append(f"WHILE: condition {ast.dump(node.test)}")
        self.generic_visit(node)

    def visit_Try(self, node):
        """Detect try/except/finally blocks"""
        self.branches.append("TRY block")
        self.generic_visit(node)
        for handler in node.handlers:
            self.branches.append(f"EXCEPT: {ast.dump(handler.type) if handler.type else 'Any exception'}")
        if node.finalbody:
            self.branches.append("FINALLY block")

def analyze_code(code):
    tree = ast.parse(code)
    analyzer = BranchAnalyzer()
    analyzer.visit(tree)
    return analyzer.branches

# Example code to analyze
# example_code = """
# def example(x):
#     if x > 0:
#         print("Positive")
#     elif x < 0:
#         print("Negative")
#     else:
#         print("Zero")

#     for i in range(3):
#         print(i)

#     try:
#         risky_function()
#     except ValueError:
#         print("Caught a ValueError")
#     finally:
#         print("Cleanup")
# """

# branches = analyze_code(example_code)
# for branch in branches:
#     print(branch)


