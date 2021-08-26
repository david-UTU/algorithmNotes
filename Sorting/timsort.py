#This is a combination of insertion sort and merge sort
#Uses insertion sort to divide an array into x num of sublists | x is the min run
#Then begin merging the sorted lists
#Calculate your midpoint (end of array 1) and endpoint (end of array 2)
#Merge your arrays
#Each iteration doubles the length of the list until at the desired size
def insertionSort(a_list):
    indexing_length = range(1,len(a_list))
    for i in indexing_length:
        value = a_list[i]
        while a_list[i-1] > value and i>0:
            a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
            i = i-1
    return a_list

def timSort(a_list):
    min_run = 32
    n = len(a_list)
    for i in range(0, n, min_run):
        insertion_sort(a_list, i, min((i + min_run - 1), n - 1))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merged_array = merge(
                left=a_list[start:midpoint + 1],
                right=a_list[midpoint + 1:end + 1])
            a_list[start:start + len(merged_array)] = merged_array
        size *= 2
    return a_list