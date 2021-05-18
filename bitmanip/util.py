from typing import *
import builtins

def hex(o: object):
    if isinstance(o, int):
        return builtins.hex(o)
    elif isinstance(o, tuple):
        return tuple(map(builtins.hex, o))
    elif isinstance(o, list):
        return list(map(builtins.hex, o))
    else:
        raise TypeError("invalid type to hex")

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

def bits(n: int, bits: int) -> int:
    return n & (2 ** bits - 1)

def split8(n: int) -> Tuple[int, int]:
    return (bits(bits(n, 16) >> 8, 8), bits(n, 8))

def cat8(h: int, l: int) -> int:
    return bits((bits(h, 8) << 8) | bits(l, 8), 16)

def split16(n: int) -> Tuple[int, int]:
    return (bits(bits(n, 32) >> 16, 16), bits(n, 16))

def cat16(h: int, l: int) -> int:
    return bits((bits(h, 16) << 16) | bits(l, 16), 32)

def split32(n: int) -> Tuple[int, int]:
    return (bits(bits(n, 64) >> 32, 32), bits(n, 32))

def cat32(h: int, l: int) -> int:
    return bits((bits(h, 32) << 32) | bits(l, 32), 64)
