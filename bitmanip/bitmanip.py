from . import util
from . import base

def clz32(n: int) -> int:
    n = util.bits(n, 32)
    for i in range(32):
        if (n << i) >> 31:
            return i
    return 32

def clz64(n: int) -> int:
    n = util.bits(n, 64)
    for i in range(64):
        if (n << i) >> 63:
            return i
    return 64

def ctz32(n: int) -> int:
    n = util.bits(n, 32)
    for i in range(32):
        if (n >> i) & 1:
            return i
    return 32

def ctz64(n: int) -> int:
    n = util.bits(n, 64)
    for i in range(64):
        if (n >> i) & 1:
            return i
    return 64

def cpop32(n: int) -> int:
    n = util.bits(n, 32)
    x = 0
    for i in range(32):
        x += (n >> i) & 1
    return x

def cpop64(n: int) -> int:
    n = util.bits(n, 64)
    x = 0
    for i in range(64):
        x += (n >> i) & 1
    return x

def andn32(n1: int, n2: int) -> int:
    return base.and32(n1, ~n2)

def andn64(n1: int, n2: int) -> int:
    return base.and64(n1, ~n2)

def orn32(n1: int, n2: int) -> int:
    return base.or32(n1, ~n2)

def orn64(n1: int, n2: int) -> int:
    return base.or64(n1, ~n2)

def xnor32(n1: int, n2: int) -> int:
    return base.xor32(n1, ~n2)

def xnor64(n1: int, n2: int) -> int:
    return base.xor64(n1, ~n2)

def sextb32(n: int) -> int:
    return util.sext(n, 8, 32)

def sextb64(n: int) -> int:
    return util.sext(n, 8, 64)

def sexth32(n: int) -> int:
    return util.sext(n, 16, 32)

def sexth64(n: int) -> int:
    return util.sext(n, 16, 64)

def sextw64(n: int) -> int:
    return util.sext(n, 32, 64)

def slo32(n: int, r: int) -> int:
    return util.bits(~base.sll32(~n, r), 32)

def slo64(n: int, r: int) -> int:
    return util.bits(~base.sll64(~n, r), 64)

def sro32(n: int, r: int) -> int:
    return util.bits(~base.srl32(~n, r), 32)

def sro64(n: int, r: int) -> int:
    return util.bits(~base.srl64(~n, r), 64)

def rol32(n: int, r: int) -> int:
    return base.sll32(n, r) | base.srl32(n, 32 - r)

def rol64(n: int, r: int) -> int:
    return base.sll64(n, r) | base.srl64(n, 64 - r)

def ror32(n: int, r: int) -> int:
    return base.srl32(n, r) | base.sll32(n, 32 - r)

def ror64(n: int, r: int) -> int:
    return base.srl64(n, r) | base.sll64(n, 64 - r)
