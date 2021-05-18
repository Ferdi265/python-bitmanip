from . import util
from . import misc
from . import permutation

def bmatflip64(n: int) -> int:
    n = permutation.shfl64.zip(n)
    n = permutation.shfl64.zip(n)
    n = permutation.shfl64.zip(n)
    return n

def bmatxor64(n1: int, n2: int) -> int:
    n2 = bmatflip64(n2)

    u = [0] * 8
    v = [0] * 8

    for i in range(8):
        u[i] = util.bits(n1 >> (i * 8), 8)
        v[i] = util.bits(n2 >> (i * 8), 8)

    x = 0
    for i in range(64):
        if misc.cpop64(u[i // 8] & v[i % 8]) & 1:
            x |= 1 << i
    return x

def bmator64(n1: int, n2: int) -> int:
    n2 = bmatflip64(n2)

    u = [0] * 8
    v = [0] * 8

    for i in range(8):
        u[i] = util.bits(n1 >> (i * 8), 8)
        v[i] = util.bits(n2 >> (i * 8), 8)

    x = 0
    for i in range(64):
        if misc.cpop64(u[i // 8] & v[i % 8]) != 0:
            x |= 1 << i
    return x
