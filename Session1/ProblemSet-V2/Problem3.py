'''Given an integer list nums of length n, create a function concatenate_list() that creates and returns a list ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums lists.

def concatenate_list(nums):
    pass
Example Input: [1,2,3,4]
Example Output: [1,2,3,4,1,2,3,4]'''

def concatenate_list(nums):
    ans = []
    for num in nums:
        ans.append(num)
    for num in nums:
        ans.append(num)
    return ans

finalList = concatenate_list([1, 2, 3, 4])  # Example usage
print(finalList)
