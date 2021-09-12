from functools import reduce


def roman(aString):
    equivalences = {"I": 1, "V": 5, "X": 10,
                    "L": 50, "C": 100, "D": 500, "M": 1000}
    number = reduce(lambda val, i: val + (-equivalences[aString[i]] if equivalences[aString[i]] < equivalences[aString[i+1]]
                    else equivalences[aString[i]]), reversed(range(len(aString)-1)), equivalences[aString[-1]])
    return number


num = str(input("Input roman numeral here:\n"))
print(roman(num))
