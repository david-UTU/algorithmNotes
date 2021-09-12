def multiply(x, y):
    def add(a, b):
        return a if b == 0 else add(a^b, (a&b) << 1)

    total = 0
    while x:
        if x & 1:
            total = add(total, y)
        x, y = x >> 1, y << 1
    return total


print(multiply(50, 4))
