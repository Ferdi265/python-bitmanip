from . import util

def pack16(n1: int, n2: int) -> int:
    l, _ = util.split8(n1)
    h, _ = util.split8(n2)
    return util.cat8(l, h)

def packu16(n1: int, n2: int) -> int:
    _, l = util.split8(n1)
    _, h = util.split8(n2)
    return util.cat8(l, h)

def pack32(n1: int, n2: int) -> int:
    l, _ = util.split16(n1)
    h, _ = util.split16(n2)
    return util.cat16(l, h)

def packu32(n1: int, n2: int) -> int:
    _, l = util.split16(n1)
    _, h = util.split16(n2)
    return util.cat16(l, h)

def pack64(n1: int, n2: int) -> int:
    l, _ = util.split32(n1)
    h, _ = util.split32(n2)
    return util.cat32(l, h)

def packu64(n1: int, n2: int) -> int:
    _, l = util.split32(n1)
    _, h = util.split32(n2)
    return util.cat32(l, h)

def bset32(n: int, b: int) -> int:
    n = util.bits(n, 32)
    b = util.bits(n, 5)
    return n | (1 << b)

def bset64(n: int, b: int) -> int:
    n = util.bits(n, 64)
    b = util.bits(n, 6)
    return n | (1 << b)

def bclr32(n: int, b: int) -> int:
    n = util.bits(n, 32)
    b = util.bits(n, 5)
    return n & ~(1 << b)

def bclr64(n: int, b: int) -> int:
    n = util.bits(n, 64)
    b = util.bits(n, 6)
    return n & ~(1 << b)

def binv32(n: int, b: int) -> int:
    n = util.bits(n, 32)
    b = util.bits(n, 5)
    return n ^ (1 << b)

def binv64(n: int, b: int) -> int:
    n = util.bits(n, 64)
    b = util.bits(n, 6)
    return n ^ (1 << b)

def bext32(n: int, b: int) -> int:
    n = util.bits(n, 32)
    b = util.bits(n, 5)
    return (n >> b) & 1

def bext64(n: int, b: int) -> int:
    n = util.bits(n, 64)
    b = util.bits(n, 6)
    return (n >> b) & 1
