#Parity of a binary word is 1 if the number of 1s in the binary word sequence is 1
#Useful for detecting single bit errors in data

def bruteParity(x): #tests the value of each individual bit
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result
    #Time complexity is O(n) where n = word size

def dropParity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1 #Drops the lowest set bit of x


