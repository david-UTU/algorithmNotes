def swapBits(x, i, j):
    #extract the i-th and j-th bits and compare them
    if (x >> i) & 1 != (x >> j) & 1:
        bitMask = (1 << i) | (1 << j)
        x ^= bitMask
    return x


