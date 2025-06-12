def get_last(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[len(lst) - 1]
    
num = get_last([2, 3, 4, 5])
print(num)