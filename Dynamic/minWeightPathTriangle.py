def minWeight(triList):
    minToCurr = [0]
    for row in triList:
        minToCurr[row[j]+min(minToCurr[max(j-1, 0)], minToCurr[min(j, len(minToCurr)-1)]) for j in range(len(row))]
    return min(minToCurr)

