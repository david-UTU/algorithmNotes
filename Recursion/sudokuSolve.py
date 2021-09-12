

def solve(partList):

    def partialSolve(i, j):
        if i == len(partList):
            i = 0
            j += 1
            if j == len(partList[i]):
                return True #means the whole thing was filled

        if partList != emptyEntry:
            return partialSolve(i+1, j)

        def validAddition(i, j, val):
            if any(val == partList[k][j] for k in range(len(partList))):
                return False

            if val in partList[i]:
                return False

            region = int(math.sqrt(len(partList)))
            I, J = i, j
            return not any(val == partList[region* I + a][region*J+b] for a, b in itertools.product(range(region), repeat=2))

        for val in range(1, len(partList)+1):
            if validAddition(i, j, val):
                partList[i][j] = val
                if partialSolve(i + 1, j):
                    return True

        partList[i][j] = emptyEntry
        return False

    emptyEntry = 0
    return partialSolve(0, 0)


