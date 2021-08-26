class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
def reverseLinkedList(head):
    curr = head
    prev = None
    while True:
        temp = curr.next
        curr.next = prev
        prev = curr
        if not temp:
            break
        curr = temp
    return curr
