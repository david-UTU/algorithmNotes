def change(cents):
    coinOptions = [100, 50, 25, 10, 5, 1]
    amountRequired = 0
    for i in coinOptions:
        amountRequired += cents // i
        cents %= i
    return amountRequired

cents = int(input("Amount:\n"))

print(change(cents))
