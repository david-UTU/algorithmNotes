def recursive_binary(a_list, target):
    if len(a_list) == 0:
        #checks if the list is empty
        return False
    else:
        middle = len(a_list)//2
        if a_list[middle] == target:
            return True
        else:
            if a_list[middle] < target:
                #resort to recursion
                return recursive_binary(a_list[middle+1:], target)
            else:
                return recursive_binary(a_list[:middle], target)

def verify(result):
    print(f"Target found: {result}")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary(numbers, 6)
verify(result)