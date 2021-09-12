def linear_search(a_list, target):
    #returns index of target if found, else none
    for i in range(0, len(a_list)):
        if a_list[i] == target:
            return i
    return None

def verify(i):
    if i != None:
        print(f'Target number is at index {i}')
    else:
        print('Target not found in list')
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = linear_search(numbers, 6)
verify(result)
