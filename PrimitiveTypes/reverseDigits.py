def reverse(x):
    result, xRemaining = 0, abs(x)
    while xRemaining:
        result = result*10 + xRemaining%10
        xRemaining//=10
    return -result if x < 0 else result

x = int(input("What digit would you like to reverse?\n"))

print(reverse(x))
