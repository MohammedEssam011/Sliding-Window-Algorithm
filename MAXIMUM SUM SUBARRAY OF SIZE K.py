"""
Given a word and a text, return the count of occurrences of the anagrams of the word in the text.

Input: text = gotxxotgxdogt, word = got
Output : 3
Words “got,” “otg” and “ogt” are anagrams of “got.”

"""

def getCountOccurances(text, word):
    wHeap = [0] * 26
    textHeap = [0] * 26
    start = 0
    count = 0
    
    for c in word:
        wHeap[ord(c) - ord('a')] += 1
    
    for i in range(len(text)):
        textHeap[ord(text[i]) - ord('a')] += 1
        if (i - start + 1) == len(word):
            if textHeap == wHeap:
                count += 1
            
            textHeap[ord(text[start]) - ord('a')] -= 1
            start += 1
        
    return count
            