#Takes a sequence and sets the last item as a pivot point
#L-R compare items in list to pivot and assign to new sublists, less than and greater than
#Repeats process on sublists until fully sorted
#Yay recursion
def quickSort(a_list):
    indexing_length = len(a_list)
    if indexing_length <=1:
        return a_list
    else:
        pivot = a_list.pop()
        #pop removes the final element and returns it
    greater = []
    lower = []

    for i in a_list:
        if i > pivot:
            greater.append[i]
        else:
            lower.append[i]
    return quicksort(lower) + [pivot] + quicksort(greater)