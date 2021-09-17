"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ord_1 = [ord(s) - ord('a') for s in s1]
        ord_2 = [ord(s) - ord('a') for s in s2]
        
        target = [0] * 26
        for i in ord_1:
            target[i] += 1
            
        window = [0] * 26
        
        for i, value in enumerate(ord_2):
            window[value] += 1
            
            if i >= len(ord_1):
                window[ord_2[i-len(ord_1)]] -= 1
            if window == target:
                return True
            
        return False