import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def is_sorted(values):
    for i in range(len(values)-1):
        if values[i] > values[i+1]:
            return False
    return True

def bogosort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values

print(bogosort(numbers))