def max_heap(a_list, n, parentIndex):
    largest = parentIndex
    left = 2*parentIndex + 1
    right 2*parentIndex + 2
    if left < n and a_list[left] > a_list[largest]:
        largest = left
    if right < n and a_list[right] > a_list[largest]:
        largest = right
    if largest != parentIndex:
        a_list[largest], a_list[parentIndex] = a_list[parentIndex], a_list[largest]
        max_heap(a_list, n, largest) 
def heapSort(a_list):
    n = len(a_list)
    #create a max heap from the array
    for i in range(n//2 - 1, -1, -1): 
        #range is floor div2n -1 as the start, goes to final position, all in reverse order
        max_heap(a_list, n, i)
    for i in range(n-1, 0, -1):
        a_list[i], a_list[0] = a_list[0], a_list[i]
        max_heap(a_list, i, 0)