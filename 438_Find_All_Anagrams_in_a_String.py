"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ord_s = [0] * 26
        ord_p = [0] * 26
        
        for i in range(len(p)):
            ord_p[ord(p[i]) - 97] += 1
            
        i = 0
        ans = []
        
        for j in range(len(s)):
            ord_s[ord(s[j]) - 97] += 1
            
            if j - i == len(p):
                ord_s[ord(s[i]) - 97] -= 1
                i += 1
            
            if ord_s == ord_p:
                ans.append(i)
        
        return ans
            