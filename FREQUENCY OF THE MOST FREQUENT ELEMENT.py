"""
FREQUENCY OF THE MOST FREQUENT ELEMENT
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
"""
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        len_nums = len(nums)
        nums.sort()
        max_freq = 1
        freq = 1
        left = 0
        ops = k
        
        for right in range(1, len_nums):
            ops -= (nums[right] - nums[right - 1]) * freq
            freq += 1
            if ops >= 0:
                max_freq = max(max_freq, freq)
            else:
                while ops < 0:
                    ops += nums[right] - nums[left]
                    left += 1
                    freq -= 1
                    
        return max_freq