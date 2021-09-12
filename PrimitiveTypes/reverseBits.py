# Reverses bits, duh
# Uses an array lookup table where for every 16 bit integer, the corresponding value holds the bit-reversal of y
# Finish later and define Precomputed
def reverseBits(x):
    maskSize = 16
    bitMask = 0xFFFF
    reverse = (PRECOMPUTED_REVERSE[x & bitMask] << (3*maskSize) | PRECOMPUTED_REVERSE[(x >> maskSize) & bitMask] << (2*maskSize)
               | PRECOMPUTED_REVERSE[(x >> (2*maskSize)) & bitMask] << maskSize
               | PRECOMPUTED_REVERSE[(x >> (3*maskSize)) & bitMask])
    return reverse


print(reverseBits(11001001))
