def hasTwo(numList, target):
    i, j = 0, len(numList) - 1
    while i <= j:
        if numList[i] + numList[j] == target:
            return True
        elif numList[i] + numList[j] < target:
            i += 1
        else:
            j -= 1
    return False


def hasThree(numList, target):
    numList.sort()
    return any(hasTwo(numList, target - i) for i in numList)
