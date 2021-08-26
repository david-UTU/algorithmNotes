#Takes an unsorted sequence, divides into two lists (sorted and unsorted)
#Then l-r items are added to the sorted list and compared to other values in the list r-l
#Items are switched until in the correct order

def insertionSort(a_list):
    indexing_length = range(1,len(a_list))
    for i in indexing_length:
        value = a_list[i]
        while a_list[i-1] > value and i>0:
            a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
            i = i-1
    return a_list

