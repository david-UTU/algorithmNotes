def uniformRand(lower, upper):
    outcomes = upper - lower + 1
    while True:
        result, i = 0, 0
        while (1 << i) < outcomes:
            result = (result << 1) | zero_one_random()
            i += 1
        if result < outcomes:
            break
    return result + lower

lower, upper = map(int, input("Upper and Lower Bounds, please:\n").split())

print(uniformRand(lower, upper))
