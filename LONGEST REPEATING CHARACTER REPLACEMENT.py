"""
COUNT DISTINCT ABSOLUTE VALUES IN A SORTED ARRAY
Input:  { -1, -1, 0, 1, 1, 1 }
Output: The total number of distinct absolute values is 2 (0 and 1)
"""

def getCountDistinct(arr):
    count = 0
    d = {}
    for item in arr:
        if item >= 0 and item not in d:
            d[item] = 1
            count += 1
    
    return count