"""
 FIND ALL ANAGRAMS IN A STRING
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""

def findAnagrams(s, p):
    target = [0] *  26
    result = []
    count = [0] * 26
    start = 0
    
    for c in p:
        target[ord(c) - ord('a')] += 1
   
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        if i - start == len(p):
            count[ord(s[start]) - ord('a')] -= 1
            start += 1
        
        if count == target:
            result.append(start)
    return result