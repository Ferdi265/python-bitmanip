from . import util
from . import base

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

def fsl32(n1: int, n2: int, r: int) -> int:
    return util.bits((((util.bits(n1, 32) << 32) | util.bits(n2, 32)) << util.bits(r, 5)) >> 32, 32)

def fsl64(n1: int, n2: int, r: int) -> int:
    return util.bits((((util.bits(n1, 64) << 64) | util.bits(n2, 64)) << util.bits(r, 6)) >> 64, 64)

def fsr32(n1: int, n2: int, r: int) -> int:
    return util.bits(((util.bits(n1, 32) << 32) | util.bits(n2, 32)) >> util.bits(r, 5), 32)

def fsr64(n1: int, n2: int, r: int) -> int:
    return util.bits(((util.bits(n1, 64) << 64) | util.bits(n2, 64)) >> util.bits(r, 6), 64)
