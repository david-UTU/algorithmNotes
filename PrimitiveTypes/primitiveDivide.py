def divide(x, y):
    result, power = 0, 32
    yPower = y << power
    while x >= y:
        while yPower > x:
            yPower >>= 1
            power -= 1
        result += 1 << power
        x -= yPower
    return result

print(divide(50, 5))
