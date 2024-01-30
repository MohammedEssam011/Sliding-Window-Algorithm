"""
PERMUTATION IN STRING
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1’s permutations is the substring of s2.

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
"""

def checkInclusion(self, s1, s2):
    numbers = [0]*26
    numbers2 = [0]*26
    
    for c in s1:
        numbers[ord(c) - ord('a')] += 1
        
    for index in range(0, len(s2)):
        numbers2[ord(s2[index]) - ord('a')] += 1
        
        if index >= len(s1) - 1:
            if numbers == numbers2:
                return True
                
            numbers2[ord(s2[index - len(s1) + 1]) - ord('a')] -= 1
                
    return False