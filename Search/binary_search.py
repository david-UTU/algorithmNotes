def binary_search(a_list, target):
    first = 0
    last = len(a_list)-1
    while first <= last:
        middle = (first+last)//2
        #use floor division because it rounds down to nearest whole
        if a_list[middle] == target:
            return middle
        elif a_list[middle] < target:
            first = middle + 1
        else:
            last = middle - 1
    return None

def verify(i):
    if i != None:
        print(f'Target number is at index {i}')
    else:
        print('Target not found in list')
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = binary_search(numbers, 6)
verify(result)