from typing import Optional

from dynapyt.analyses.BaseAnalysis import BaseAnalysis


class BranchCoverage(BaseAnalysis):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.branches = dict()
        self.iids = set()

    def enter_control_flow(self, dyn_ast: str, iid: int, cond_value: bool) -> Optional[bool]:
        self.branches[(iid, bool(cond_value))] = self.branches.get((iid, bool(cond_value)), 0) + 1
        self.iids.add(iid)
    
    def end_execution(self):
        total_branches = len(self.iids) * 2 # true and false
        for k, v in self.branches.items():
            print(f'Branch {k[0]} taken with condition {k[1]}, {v} time{"" if v == 1 else "s"}')
            # if k[1]:

        covered_branches = len(self.branches)
        print("branches", self.branches)
        print("covered branches", covered_branches)
        print("total branches", total_branches)
        print(f'Percent {(covered_branches / total_branches) * 100}%')
