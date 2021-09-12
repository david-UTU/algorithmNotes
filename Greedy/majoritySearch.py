def majority(longString):
    candidateCount = 0
    for i in longString:
        if candidateCount == 0:
            candidate, candidateCount = i, candidateCount + 1
        elif candidate == i:
            candidateCount += 1
        else:
            candidateCount -= 1
    return candidate

randString = "aasdsaasngbbbbskxxxxwtnggsapp"

print(majority(randString))
