"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = ""
        
        for char in s:
            if char.isalpha():
                cleaned += char.lower()
            elif char.isnumeric():
                cleaned += char
                
        if len(cleaned) == 1: return True
        
        return self.check(cleaned, 0, len(cleaned) - 1)
    
    def check(self, s, i, j):
        print(i, j)

        if i >= j:
            return True

        if s[i] != s[j]: 
            return False
        
        return self.check(s, i + 1, j - 1)
