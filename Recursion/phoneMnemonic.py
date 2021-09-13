Mapping = ('0','1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ')

def phoneMnemonic(number): #takes in phone number as a string
    def helper(digit):
        if digit == len(number):
            mnemonics.append(''.join(partialMnemonic))
        else: 
            for c in Mapping[int(number[digit])]:
                partialMnemonic[digit] = c
                helper(digit+1)

    mnemonics = []
    partialMnemonic = ['0'] * len(number)
    helper(0)
    return mnemonics

number = input("What number would you like to run through?\n")

print(phoneMnemonic(number))
