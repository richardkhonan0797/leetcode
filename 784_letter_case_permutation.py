"""
Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: s = "12345"
Output: ["12345"]
Example 4:

Input: s = "0"
Output: ["0"]
"""

from typing import List


class Solution:
    def __init__(self):
        
        self.res = []

    def letterCasePermutation(self, s: str) -> List[str]:
        
        self.backtrack(s, "", 0)
        
        return self.res
        
    def backtrack(self, s, curr, i):
        
        if len(curr) == len(s):
            self.res.append(curr)
            return
            
        if s[i].isalpha():
            self.backtrack(s, curr + s[i].swapcase(), i + 1)
        
        self.backtrack(s, curr + s[i], i + 1)
        