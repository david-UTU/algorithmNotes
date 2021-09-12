def perms(aList):

    def directedPerms(i):
        if i == (len(aList)-1):
            result.append(aList.copy())
            return

        for x in range(i, len(aList)):
            aList[i], aList[x] = aList[x], aList[i]
            directedPerms(i+1)
            aList[i], aList[x] = aList[x], aList[i]
    
    result = []
    directedPerms(0)
    return result

nums = [5, 3, 7]

print(perms(nums))
