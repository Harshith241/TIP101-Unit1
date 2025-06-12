'''Write a function get_last() that takes in a list as a parameter and returns the last item in the list. Return None if the list is empty.

def get_last(lst):
    pass
Example Input: [3,1,6,7,5]
Example Output: 5'''

def get_last(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[len(lst) - 1]
    
num = get_last([2, 3, 4, 5])
print(num)