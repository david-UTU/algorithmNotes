pegCount = 3

def hanoi(rings):
    def steps(ringMoves, fromPeg, toPeg, usePeg):
        if ringMoves:
            steps((ringMoves - 1), fromPeg, usePeg, toPeg)
            pegs[toPeg].append(pegs[fromPeg].pop())
            result.append([fromPeg, toPeg])
            steps((ringMoves - 1), usePeg, toPeg, fromPeg)

    result = []
    pegs = [list(reversed(range(1, rings+1)))] + [[] for i in range(1, pegCount)]
    steps(rings, 0, 1, 2)
    return result

print(hanoi(6))
