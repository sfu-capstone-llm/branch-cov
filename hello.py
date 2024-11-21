import ast
from typing import Optional

from dynapyt.analyses.BaseAnalysis import BaseAnalysis
from branch_analyzer import analyze_code

def count_while_and_if_statements(source_code):
    # Parse the source code into an AST
    tree = ast.parse(source_code)
    
    # Initialize counters
    while_count = 0
    if_count = 0

    # Traverse the AST
    for node in ast.walk(tree):
        if isinstance(node, ast.While):
            while_count += 1
        elif isinstance(node, ast.If):
            if_count += 1

    return while_count, if_count

class BranchCoverage(BaseAnalysis):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.branches = dict()
        self.iids = set()
        self.all_branches = None

    def enter_control_flow(self, dyn_ast: str, iid: int, cond_value: bool) -> Optional[bool]:
        if not self.all_branches:
            print("a", dyn_ast)
            f = open(dyn_ast, "r")
            self.all_branches = analyze_code(f.read())
        print(f.read())
        self.branches[(iid, bool(cond_value))] = self.branches.get((iid, bool(cond_value)), 0) + 1
        self.iids.add(iid)
    
    def end_execution(self):
        total_branches = len(self.all_branches) * 2 # true and false
        for k, v in self.branches.items():
            print(f'Branch {k[0]} taken with condition {k[1]}, {v} time{"" if v == 1 else "s"}')

        covered_branches = len(self.branches)
        print("branches", self.branches)
        print("covered branches", covered_branches)
        print("total branches", total_branches)
        print(f'Percent {(covered_branches / total_branches) * 100}%')
