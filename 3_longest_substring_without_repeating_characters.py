"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0
"""

def lengthOfLongestSubstring(s: str) -> int:       
    chars = {}
    
    longest = 0
    cur_len = 0
    cur_start = 0
    
    for i, char in enumerate(s):
        if char in chars and chars[char] >= cur_start:
            cur_len = i - chars[char]    
            cur_start = chars[char] + 1
            chars[char] = i
        else:
            chars[char] = i
            cur_len += 1
            if cur_len > longest:
                longest = cur_len
                
    return longest

print(lengthOfLongestSubstring(s="abcabcbb"))
print(lengthOfLongestSubstring(s="bbbbb"))
print(lengthOfLongestSubstring(s="pwwkew"))
print(lengthOfLongestSubstring(s=""))
