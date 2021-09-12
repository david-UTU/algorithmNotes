def closest(x):
    unsignedBits = 64
    for i in range(unsignedBits-1):
        if (x >> i) & 1 != (x >> (i+1)) & 1:
            x ^= (1 << i) | (1 << (i + 1)) #swaps bit i and bit i + 1
            return x
    raise ValueError('All bits are 0 or 1')

print(closest(1011))
