# DYNAPYT: DO NOT INSTRUMENT

# https://github.com/sola-st/DynaPyt/blob/main/tutorial/task2/main.py

from dynapyt.runtime import RuntimeEngine
_rt = RuntimeEngine()

_dynapyt_ast_ = "/Users/marcus/repos/branch-cov/program1.py" + ".orig"
try:
    a = 10
    if _rt._enter_if_(_dynapyt_ast_, 2, a < 20):
        b = 20
        while _rt._enter_while_(_dynapyt_ast_, 0, a < b):
            a += 1
            if _rt._enter_if_(_dynapyt_ast_, 1, a == 15):
                continue
            print(a)
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)

