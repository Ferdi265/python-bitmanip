from . import util

def lui32(n: int) -> int:
    return util.bits(n << 12, 32)

def add32(n1: int, n2: int) -> int:
    return util.bits(util.bits(n1, 32) + util.bits(n2, 32), 32)

def add64(n1: int, n2: int) -> int:
    return util.bits(util.bits(n1, 64) + util.bits(n2, 64), 64)

def sub32(n1: int, n2: int) -> int:
    return util.bits(util.bits(n1, 32) - util.bits(n2, 32), 32)

def sub64(n1: int, n2: int) -> int:
    return util.bits(util.bits(n1, 64) - util.bits(n2, 64), 64)

def and32(n1: int, n2: int) -> int:
    return util.bits(n1, 32) & util.bits(n2, 32)

def and64(n1: int, n2: int) -> int:
    return util.bits(n1, 64) & util.bits(n2, 64)

def or32(n1: int, n2: int) -> int:
    return util.bits(n1, 32) | util.bits(n2, 32)

def or64(n1: int, n2: int) -> int:
    return util.bits(n1, 64) | util.bits(n2, 64)

def xor32(n1: int, n2: int) -> int:
    return util.bits(n1, 32) ^ util.bits(n2, 32)

def xor64(n1: int, n2: int) -> int:
    return util.bits(n1, 64) ^ util.bits(n2, 64)

def sll32(n: int, r: int) -> int:
    return util.bits(util.bits(n, 32) << util.bits(r, 5), 32)

def sll64(n: int, r: int) -> int:
    return util.bits(util.bits(n, 64) << util.bits(r, 6), 64)

def srl32(n: int, r: int) -> int:
    return util.bits(n, 32) >> util.bits(r, 5)

def srl64(n: int, r: int) -> int:
    return util.bits(n, 64) >> util.bits(r, 6)

def sra32(n: int, r: int) -> int:
    return util.sext(n, 32, 64) >> util.bits(r, 5)

def sra64(n: int, r: int) -> int:
    return util.sext(n, 64, 128) >> util.bits(r, 6)
