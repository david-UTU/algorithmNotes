#takes a list and orders it in ascending values
def bubbleSort(a_list):
    indexing_length = len(a_list)-1
    sort = False
    while not sort:
        sort = True
        for i in range(0, indexing_length):
            if a_list[i] > a_list[i+1]:
                sort = False
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
    return a_list

print(bubbleSort([4,5,3,5,2,6,8,8,2]))