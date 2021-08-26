#looking through a list is slower than looking up elements in a dictionary (hash table)

def largestRange(a_list):
    numbers = {i:0 for i in a_list}
    left = 0
    right = 0

    for n in a_list:
        if numbers[n] == 0:
            leftcount = n - 1
            rightcount = n + 1
        while leftcount in numbers:
            numbers[leftcount] = 1
            leftcount -= 1
        leftcount += 1
        
        while rightcount in numbers:
            numbers[rightcount] = 1
            rightcount += 1
        rightcount -= 1

        if (right-left) <= (rightcount-leftcount):
            right = rightcount
            left = leftcount

    return [left, right]

a_list = [1,11,3,0,15,5,2,4,10,12,7,6]

print(largestRange(a_list))