#Tries to find the minimum value in a list
#Set the first value as a minimum, then compare to the values to the right
#When true minimum is found, it is sent to a separate sorted list
#Process repeats until sorted in ascending order
def selectionSort(a_list):
    indexing_length = range(0,len(a_list)-1)
    for i in indexing_length:
        minimum = i
        for x in range(i+1, len(a_list)):
            if a_list[x] < a_list[minimum]:
                minimum = x
        if minimum != i:
            a_list[minimum], a_list[i] = a_list[i], a_list[minimum]
    return a_list