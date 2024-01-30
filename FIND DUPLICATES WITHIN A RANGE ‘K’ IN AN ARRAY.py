"""
FIND DUPLICATES WITHIN A RANGE ‘K’ IN AN ARRAY
​Input: nums = [5, 6, 8, 2, 4, 6, 9]
k = 2
Ouput: False
"""

def getDuplicates(nums, k):
    d = {}
    count = 0
    for i in range(len(nums)):
        if nums[i] in d and i - d[nums[i]] <= k:
            return True
        else:
            d[nums[i]] = i
    
    return False]
            