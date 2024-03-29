from . import internal
from . import util
from . import base

@internal.callobj
def grev32(n: int, m: int) -> int:
    n = util.bits(n, 32)
    m = util.bits(m, 5)
    if m &  1: n = base.sll32(n & 0x55555555,  1) | base.srl32(n & 0xAAAAAAAA,  1)
    if m &  2: n = base.sll32(n & 0x33333333,  2) | base.srl32(n & 0xCCCCCCCC,  2)
    if m &  4: n = base.sll32(n & 0x0F0F0F0F,  4) | base.srl32(n & 0xF0F0F0F0,  4)
    if m &  8: n = base.sll32(n & 0x00FF00FF,  8) | base.srl32(n & 0xFF00FF00,  8)
    if m & 16: n = base.sll32(n & 0x0000FFFF, 16) | base.srl32(n & 0xFFFF0000, 16)
    return n

grev32.revp  = internal.bind2(grev32, 0b00001)
grev32.rev2n = internal.bind2(grev32, 0b00010)
grev32.revn  = internal.bind2(grev32, 0b00011)
grev32.rev4b = internal.bind2(grev32, 0b00100)
grev32.rev2b = internal.bind2(grev32, 0b00110)
grev32.revb  = internal.bind2(grev32, 0b00111)
grev32.rev8h = internal.bind2(grev32, 0b01000)
grev32.rev4h = internal.bind2(grev32, 0b01100)
grev32.rev2h = internal.bind2(grev32, 0b01110)
grev32.revh  = internal.bind2(grev32, 0b01111)
grev32.rev16 = internal.bind2(grev32, 0b10000)
grev32.rev8  = internal.bind2(grev32, 0b11000)
grev32.rev4  = internal.bind2(grev32, 0b11100)
grev32.rev2  = internal.bind2(grev32, 0b11110)
grev32.rev   = internal.bind2(grev32, 0b11111)

@internal.callobj
def grev64(n: int, m: int) -> int:
    n = util.bits(n, 64)
    m = util.bits(m, 6)
    if m &  1: n = base.sll64(n & 0x5555555555555555,  1) | base.srl64(n & 0xAAAAAAAAAAAAAAAA,  1)
    if m &  2: n = base.sll64(n & 0x3333333333333333,  2) | base.srl64(n & 0xCCCCCCCCCCCCCCCC,  2)
    if m &  4: n = base.sll64(n & 0x0F0F0F0F0F0F0F0F,  4) | base.srl64(n & 0xF0F0F0F0F0F0F0F0,  4)
    if m &  8: n = base.sll64(n & 0x00FF00FF00FF00FF,  8) | base.srl64(n & 0xFF00FF00FF00FF00,  8)
    if m & 16: n = base.sll64(n & 0x0000FFFF0000FFFF, 16) | base.srl64(n & 0xFFFF0000FFFF0000, 16)
    if m & 32: n = base.sll64(n & 0x00000000FFFFFFFF, 32) | base.srl64(n & 0xFFFFFFFF00000000, 32)
    return n

grev64.revp   = internal.bind2(grev64, 0b000001)
grev64.rev2n  = internal.bind2(grev64, 0b000010)
grev64.revn   = internal.bind2(grev64, 0b000011)
grev64.rev4b  = internal.bind2(grev64, 0b000100)
grev64.rev2b  = internal.bind2(grev64, 0b000110)
grev64.revb   = internal.bind2(grev64, 0b000111)
grev64.rev8h  = internal.bind2(grev64, 0b001000)
grev64.rev4h  = internal.bind2(grev64, 0b001100)
grev64.rev2h  = internal.bind2(grev64, 0b001110)
grev64.revh   = internal.bind2(grev64, 0b001111)
grev64.rev16w = internal.bind2(grev64, 0b010000)
grev64.rev8w  = internal.bind2(grev64, 0b011000)
grev64.rev4w  = internal.bind2(grev64, 0b011100)
grev64.rev2w  = internal.bind2(grev64, 0b011110)
grev64.revw   = internal.bind2(grev64, 0b011111)
grev64.rev32  = internal.bind2(grev64, 0b100000)
grev64.rev16  = internal.bind2(grev64, 0b110000)
grev64.rev8   = internal.bind2(grev64, 0b111000)
grev64.rev4   = internal.bind2(grev64, 0b111100)
grev64.rev2   = internal.bind2(grev64, 0b111110)
grev64.rev    = internal.bind2(grev64, 0b111111)

@internal.callobj
def gorc32(n: int, m: int) -> int:
    n = util.bits(n, 32)
    m = util.bits(m, 5)
    if m &  1: n |= base.sll32(n & 0x55555555,  1) | base.srl32(n & 0xAAAAAAAA,  1)
    if m &  2: n |= base.sll32(n & 0x33333333,  2) | base.srl32(n & 0xCCCCCCCC,  2)
    if m &  4: n |= base.sll32(n & 0x0F0F0F0F,  4) | base.srl32(n & 0xF0F0F0F0,  4)
    if m &  8: n |= base.sll32(n & 0x00FF00FF,  8) | base.srl32(n & 0xFF00FF00,  8)
    if m & 16: n |= base.sll32(n & 0x0000FFFF, 16) | base.srl32(n & 0xFFFF0000, 16)
    return n

gorc32.orcp  = internal.bind2(gorc32, 0b00001)
gorc32.orc2n = internal.bind2(gorc32, 0b00010)
gorc32.orcn  = internal.bind2(gorc32, 0b00011)
gorc32.orc4b = internal.bind2(gorc32, 0b00100)
gorc32.orc2b = internal.bind2(gorc32, 0b00110)
gorc32.orcb  = internal.bind2(gorc32, 0b00111)
gorc32.orc8h = internal.bind2(gorc32, 0b01000)
gorc32.orc4h = internal.bind2(gorc32, 0b01100)
gorc32.orc2h = internal.bind2(gorc32, 0b01110)
gorc32.orch  = internal.bind2(gorc32, 0b01111)
gorc32.orc16 = internal.bind2(gorc32, 0b10000)
gorc32.orc8  = internal.bind2(gorc32, 0b11000)
gorc32.orc4  = internal.bind2(gorc32, 0b11100)
gorc32.orc2  = internal.bind2(gorc32, 0b11110)
gorc32.orc   = internal.bind2(gorc32, 0b11111)

@internal.callobj
def gorc64(n: int, m: int) -> int:
    n = util.bits(n, 64)
    m = util.bits(m, 6)
    if m &  1: n |= base.sll64(n & 0x5555555555555555,  1) | base.srl64(n & 0xAAAAAAAAAAAAAAAA,  1)
    if m &  2: n |= base.sll64(n & 0x3333333333333333,  2) | base.srl64(n & 0xCCCCCCCCCCCCCCCC,  2)
    if m &  4: n |= base.sll64(n & 0x0F0F0F0F0F0F0F0F,  4) | base.srl64(n & 0xF0F0F0F0F0F0F0F0,  4)
    if m &  8: n |= base.sll64(n & 0x00FF00FF00FF00FF,  8) | base.srl64(n & 0xFF00FF00FF00FF00,  8)
    if m & 16: n |= base.sll64(n & 0x0000FFFF0000FFFF, 16) | base.srl64(n & 0xFFFF0000FFFF0000, 16)
    if m & 32: n |= base.sll64(n & 0x00000000FFFFFFFF, 32) | base.srl64(n & 0xFFFFFFFF00000000, 32)
    return n

gorc64.orcp   = internal.bind2(gorc64, 0b000001)
gorc64.orc2n  = internal.bind2(gorc64, 0b000010)
gorc64.orcn   = internal.bind2(gorc64, 0b000011)
gorc64.orc4b  = internal.bind2(gorc64, 0b000100)
gorc64.orc2b  = internal.bind2(gorc64, 0b000110)
gorc64.orcb   = internal.bind2(gorc64, 0b000111)
gorc64.orc8h  = internal.bind2(gorc64, 0b001000)
gorc64.orc4h  = internal.bind2(gorc64, 0b001100)
gorc64.orc2h  = internal.bind2(gorc64, 0b001110)
gorc64.orch   = internal.bind2(gorc64, 0b001111)
gorc64.orc16w = internal.bind2(gorc64, 0b010000)
gorc64.orc8w  = internal.bind2(gorc64, 0b011000)
gorc64.orc4w  = internal.bind2(gorc64, 0b011100)
gorc64.orc2w  = internal.bind2(gorc64, 0b011110)
gorc64.orcw   = internal.bind2(gorc64, 0b011111)
gorc64.orc32  = internal.bind2(gorc64, 0b100000)
gorc64.orc16  = internal.bind2(gorc64, 0b110000)
gorc64.orc8   = internal.bind2(gorc64, 0b111000)
gorc64.orc4   = internal.bind2(gorc64, 0b111100)
gorc64.orc2   = internal.bind2(gorc64, 0b111110)
gorc64.orc    = internal.bind2(gorc64, 0b111111)

def shfl32r(n: int, ml: int, mr: int, r: int) -> int:
    n = util.bits(n, 32)
    r = util.bits(r, 5)
    x = util.bits(n & ~(ml | mr), 32)
    x |= util.bits(((n << r) & ml) | ((n >> r) & mr), 32)
    return x

@internal.callobj
def shfl32(n: int, m: int, i: int) -> int:
    n = util.bits(n, 32)
    m = util.bits(m, 4)
    if i:
        if m & 1: n = shfl32r(n, 0x44444444, 0x22222222, 1)
        if m & 2: n = shfl32r(n, 0x30303030, 0x0c0c0c0c, 2)
        if m & 4: n = shfl32r(n, 0x0f000f00, 0x00f000f0, 4)
        if m & 8: n = shfl32r(n, 0x00ff0000, 0x0000ff00, 8)
    else:
        if m & 8: n = shfl32r(n, 0x00ff0000, 0x0000ff00, 8)
        if m & 4: n = shfl32r(n, 0x0f000f00, 0x00f000f0, 4)
        if m & 2: n = shfl32r(n, 0x30303030, 0x0c0c0c0c, 2)
        if m & 1: n = shfl32r(n, 0x44444444, 0x22222222, 1)
    return n

shfl32.zipn    = internal.bind23(shfl32, 0b0001, 0)
shfl32.unzipn  = internal.bind23(shfl32, 0b0001, 0)
shfl32.zip2b   = internal.bind23(shfl32, 0b0010, 0)
shfl32.unzip2b = internal.bind23(shfl32, 0b0010, 0)
shfl32.zipb    = internal.bind23(shfl32, 0b0011, 0)
shfl32.unzipb  = internal.bind23(shfl32, 0b0011, 1)
shfl32.zip4h   = internal.bind23(shfl32, 0b0100, 0)
shfl32.unzip4h = internal.bind23(shfl32, 0b0100, 0)
shfl32.zip2h   = internal.bind23(shfl32, 0b0110, 0)
shfl32.unzip2h = internal.bind23(shfl32, 0b0110, 1)
shfl32.ziph    = internal.bind23(shfl32, 0b0111, 0)
shfl32.unziph  = internal.bind23(shfl32, 0b0111, 1)
shfl32.zip8    = internal.bind23(shfl32, 0b1000, 0)
shfl32.unzip8  = internal.bind23(shfl32, 0b1000, 0)
shfl32.zip4    = internal.bind23(shfl32, 0b1100, 0)
shfl32.unzip4  = internal.bind23(shfl32, 0b1100, 1)
shfl32.zip2    = internal.bind23(shfl32, 0b1110, 0)
shfl32.unzip2  = internal.bind23(shfl32, 0b1110, 1)
shfl32.zip     = internal.bind23(shfl32, 0b1111, 0)
shfl32.unzip   = internal.bind23(shfl32, 0b1111, 1)

def shfl64r(n: int, ml: int, mr: int, r: int) -> int:
    n = util.bits(n, 64)
    r = util.bits(r, 6)
    x = util.bits(n & ~(ml | mr), 64)
    x |= util.bits(((n << r) & ml) | ((n >> r) & mr), 64)
    return x

@internal.callobj
def shfl64(n: int, m: int, i: int) -> int:
    n = util.bits(n, 64)
    m = util.bits(m, 5)
    if i:
        if m &  1: n = shfl64r(n, 0x4444444444444444, 0x2222222222222222,  1)
        if m &  2: n = shfl64r(n, 0x3030303030303030, 0x0c0c0c0c0c0c0c0c,  2)
        if m &  4: n = shfl64r(n, 0x0f000f000f000f00, 0x00f000f000f000f0,  4)
        if m &  8: n = shfl64r(n, 0x00ff000000ff0000, 0x0000ff000000ff00,  8)
        if m & 16: n = shfl64r(n, 0x0000ffff00000000, 0x00000000ffff0000, 16)
    else:
        if m & 16: n = shfl64r(n, 0x0000ffff00000000, 0x00000000ffff0000, 16)
        if m &  8: n = shfl64r(n, 0x00ff000000ff0000, 0x0000ff000000ff00,  8)
        if m &  4: n = shfl64r(n, 0x0f000f000f000f00, 0x00f000f000f000f0,  4)
        if m &  2: n = shfl64r(n, 0x3030303030303030, 0x0c0c0c0c0c0c0c0c,  2)
        if m &  1: n = shfl64r(n, 0x4444444444444444, 0x2222222222222222,  1)
    return n

shfl64.zipn    = internal.bind23(shfl64, 0b00001, 0)
shfl64.unzipn  = internal.bind23(shfl64, 0b00001, 0)
shfl64.zip2b   = internal.bind23(shfl64, 0b00010, 0)
shfl64.unzip2b = internal.bind23(shfl64, 0b00010, 0)
shfl64.zipb    = internal.bind23(shfl64, 0b00011, 0)
shfl64.unzipb  = internal.bind23(shfl64, 0b00011, 1)
shfl64.zip4h   = internal.bind23(shfl64, 0b00100, 0)
shfl64.unzip4h = internal.bind23(shfl64, 0b00100, 0)
shfl64.zip2h   = internal.bind23(shfl64, 0b00110, 0)
shfl64.unzip2h = internal.bind23(shfl64, 0b00110, 1)
shfl64.ziph    = internal.bind23(shfl64, 0b00111, 0)
shfl64.unziph  = internal.bind23(shfl64, 0b00111, 1)
shfl64.zip8w   = internal.bind23(shfl64, 0b01000, 0)
shfl64.unzip8w = internal.bind23(shfl64, 0b01000, 0)
shfl64.zip4w   = internal.bind23(shfl64, 0b01100, 0)
shfl64.unzip4w = internal.bind23(shfl64, 0b01100, 1)
shfl64.zip2w   = internal.bind23(shfl64, 0b01110, 0)
shfl64.unzip2w = internal.bind23(shfl64, 0b01110, 1)
shfl64.zipw    = internal.bind23(shfl64, 0b01111, 0)
shfl64.unzipw  = internal.bind23(shfl64, 0b01111, 1)
shfl64.zip16   = internal.bind23(shfl64, 0b10000, 0)
shfl64.unzip16 = internal.bind23(shfl64, 0b10000, 0)
shfl64.zip8    = internal.bind23(shfl64, 0b11000, 0)
shfl64.unzip8  = internal.bind23(shfl64, 0b11000, 1)
shfl64.zip4    = internal.bind23(shfl64, 0b11100, 0)
shfl64.unzip4  = internal.bind23(shfl64, 0b11100, 1)
shfl64.zip2    = internal.bind23(shfl64, 0b11110, 0)
shfl64.unzip2  = internal.bind23(shfl64, 0b11110, 1)
shfl64.zip     = internal.bind23(shfl64, 0b11111, 0)
shfl64.unzip   = internal.bind23(shfl64, 0b11111, 1)

def xperm32r(n1: int, n2: int, r: int) -> int:
    n1 = util.bits(n1, 32)
    n2 = util.bits(n2, 32)
    r = r % 5
    m = util.mask(r)
    x = 0
    for i in range(0, 32, 1 << r):
        pos = ((n2 >> i) & m) << r
        if pos < 32:
            x |= ((n1 >> pos) & m) << i
    return x

def xpermn32(n1: int, n2: int) -> int:
    return xperm32r(n1, n2, 2)

def xpermb32(n1: int, n2: int) -> int:
    return xperm32r(n1, n2, 3)

def xpermh32(n1: int, n2: int) -> int:
    return xperm32r(n1, n2, 4)

def xperm64r(n1: int, n2: int, r: int) -> int:
    n1 = util.bits(n1, 64)
    n2 = util.bits(n2, 64)
    r = r % 6
    m = util.mask(r)
    x = 0
    for i in range(0, 64, 1 << r):
        pos = ((n2 >> i) & m) << r
        if pos < 64:
            x |= ((n1 >> pos) & m) << i
    return x

def xpermn64(n1: int, n2: int) -> int:
    return xperm64r(n1, n2, 2)

def xpermb64(n1: int, n2: int) -> int:
    return xperm64r(n1, n2, 3)

def xpermh64(n1: int, n2: int) -> int:
    return xperm64r(n1, n2, 4)

def xpermw64(n1: int, n2: int) -> int:
    return xperm64r(n1, n2, 5)
