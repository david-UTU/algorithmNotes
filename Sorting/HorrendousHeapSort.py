#MaxHeap is a datatype thats a complete binary tree where every node is <= its parent
#Max value is always node 1
#This was done using a tutorial, a truly horrendous tutorial
class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap)-1)
    
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)
    
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            maxi = self.heap.pop()
            self.bubbleDown(1)
        elif len(self.heap) == 2:
            maxi = self.heap.pop()
        else:
            maxi = False
        return maxi

    def __swap(self, i, x):
        self.heap[i], self.heap[x] = self.heap[x], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
    
    def bubbleDown(self, index):
        left = index*2
        right = index*2 + 1
        largest = index
        if len(self.heap) >left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) >right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)
            

