"""
You are given an integer array of nums consisting of n elements and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10–5 will be accepted.

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
"""

def findMaxAverage(self, nums, k):
    st = 0
    max_sum = float('-inf')
    win_sum = 0.0
    
    for i in range(len(nums)):
        win_sum += nums[i]
        if i >= k-1:
            max_sum = max(win_sum, max_sum)
            win_sum -= nums[st]
            st += 1
        
    return max_sum/k