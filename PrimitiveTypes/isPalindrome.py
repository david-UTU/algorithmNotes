import math

def isPalin(x):
    if x <= 0:
        return x == 0

    numDigits = math.floor(math.log10(x)) + 1
    msdMask = 10**(numDigits-1)
    for i in range(int(numDigits//2)):
        if x // msdMask != x % 10:
            return False
        x %= msdMask
        x //= 10
        msdMask //= 100
    return True

x = int(input("What number are you checking?\n"))

print(isPalin(x))
