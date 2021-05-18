# Python `bitmanip`

Bit manipulation functions based on RISC-V BitManip extension

## Implemented Functions

All functions except the utility functions are marked with the supported bit
widths, e.g. `clz32` for 32-bit `clz`. Functions in all categories except
"Basic Bit Manipulation Utilities" are available in 32 and 64 bit variants
unless marked otherwise.

- Basic Bit Manipulation Utilities
  - `mask` (bit mask with `n` set bits)
  - `bits` (mask a number to `n` bits)
  - `sext` (sign-extend a `n` bit number to `m` bits)
  - `split`, `cat` (split a number two 8, 16, or 32 bit halves, or concatenate them)
- Basic Arithmetic and Bitwise Instructions (RISC-V Base Instructions)
  - `lui` (32 bit only)
  - `add`, `sub`
  - `and`, `or`, `xor`
  - `sll`, `srl`, `sra`
- Miscellaneous Bit Manipulation Instructions
  - `clz`, `ctz`
  - `cpop`
  - `andn`, `orn`, `xnor`
  - `pack`, `packu`
  - `sextb` `sexth` `sextw`
  - `cmix`
  - `clmul`, `clmulh`, `clmulr`
- Shift and Rotate Instructions
  - `slo`, `sro`
  - `rol`, `ror`
  - `fsl`, `fsr`
- Bit Field Instructions
  - `pack`, `packu` (16, 32, and 64 bit)
  - `bset`, `bclr`, `binv`, `bext`
  - `bfp` (not yet implemented)
  - `bcompress`, `bdecompress` (not yet implemented)
- Bit Permutation Instructions
  - `grev`
  - `gorc`
  - `shfl`
  - `xpermn`, `xpermb`, `xpermh`
  - `xpermw` (64 bit only)
- Bit Matrix Instructions
  - `bmatflip`, `bmatxor`, `bmator` (64 bit only)

The generalized bit permutation functions have named pseudo instructions as
attributes, such as `grev32.rev8`, `shfl32.zip`, or `shfl64.zip2h`. The full
list of pseudo instructions can be seen in the RISC-V BitManip extension
draft specification.

## Missing Functions

The following functions from the RISC-V BitManip extension are not (yet)
implemented:

  - `min`, `max`, `minu`, `maxu`
  - `cmov`
  - `bfp`
  - `bcompress`, `bdecompress`
  - `crc32b`, `crc32h`, `crc32w`
  - `crc32cb`, `crc32ch`, `crc32cw`
  - `crc32d`, `crc32cd` (64 bit only)
  - `sh1add`, `sh2add`, `sh3add`
  - `sh1adduw`, `sh2adduw`, `sh3adduw` (64 bit only)
  - `adduw`, `slliuw` (64 bit only)
