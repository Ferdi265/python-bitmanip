from typing import Callable

def callobj(f):
    class Obj:
        def __call__(self, *args, **kwargs):
            return f(*args, **kwargs)

        def __repr__(self):
            return repr(f)

        def _repr_pretty_(self, p, cycle):
            p.pretty(f)

    Obj.__name__ = f.__name__
    return Obj()

def bind2(f: Callable[[int, int], int], arg2: int) -> Callable[[int], int]:
    return lambda arg1: f(arg1, arg2)

def bind23(f: Callable[[int, int, int], int], arg2: int, arg3: int) -> Callable[[int], int]:
    return lambda arg1: f(arg1, arg2, arg3)
