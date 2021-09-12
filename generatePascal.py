def generatePascal(n):
    result = [[1]*(i+1) for i in range(n)]
    for i in range(n):
        for x in range(1, i):
            # Sets this entry to the sum of the two above adjacent entries
            result[i][x] = result[i - 1][j-1]+result[i-1][j]
        return result


n = int(input())
print(generatePascal(n))
