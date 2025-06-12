'''Write a function sum_ten() that returns the sum of numbers from 1 to 10.

def sum_ten():
    pass
Example Usage: output = sum_ten()
Example Result: output = 55'''

def sum_ten():
    sum = 0
    for num in range(1, 11):
        sum += num
    return sum


sum = sum_ten()
print(sum)