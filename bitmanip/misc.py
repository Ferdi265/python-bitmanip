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

def cmix32(n1: int, n2: int, n3: int) -> int:
    return util.bits((n2 & n1) | (n3 & ~n1), 32)

def cmix64(n1: int, n2: int, n3: int) -> int:
    return util.bits((n2 & n1) | (n3 & ~n1), 64)

def clmul32(n1: int, n2: int) -> int:
    n1 = util.bits(n1, 32)
    n2 = util.bits(n2, 32)
    x = 0
    for i in range(32):
        if (n2 >> i) & 1:
            x ^= util.bits(n1 << i, 32)
    return x

def clmul64(n1: int, n2: int) -> int:
    n1 = util.bits(n1, 64)
    n2 = util.bits(n2, 64)
    x = 0
    for i in range(64):
        if (n2 >> i) & 1:
            x ^= util.bits(n1 << i, 64)
    return x

def clmulh32(n1: int, n2: int) -> int:
    n1 = util.bits(n1, 32)
    n2 = util.bits(n2, 32)
    x = 0
    for i in range(1, 32):
        if (n2 >> i) & 1:
            x ^= n1 >> (32 - i)
    return x

def clmulh64(n1: int, n2: int) -> int:
    n1 = util.bits(n1, 64)
    n2 = util.bits(n2, 64)
    x = 0
    for i in range(1, 64):
        if (n2 >> i) & 1:
            x ^= n1 >> (32 - i)
    return x

def clmulr32(n1: int, n2: int) -> int:
    n1 = util.bits(n1, 32)
    n2 = util.bits(n2, 32)
    x = 0
    for i in range(32):
        if (n2 >> i) & 1:
            x ^= n1 >> (32 - i - 1)
    return x

def clmulr64(n1: int, n2: int) -> int:
    n1 = util.bits(n1, 64)
    n2 = util.bits(n2, 64)
    x = 0
    for i in range(64):
        if (n2 >> i) & 1:
            x ^= n1 >> (32 - i - 1)
    return x
