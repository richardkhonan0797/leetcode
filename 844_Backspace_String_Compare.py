"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
Example 4:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        res_1 = []
        res_2 = []
        
        skip = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "#": 
                skip += 1
                continue
                
            if skip > 0:
                skip -=1
                continue
                
            res_1.append(s[i])
        
        skip = 0
        for i in range(len(t) - 1, -1, -1):
            if t[i] == "#": 
                skip += 1
                continue
                
            if skip > 0:
                skip -=1
                continue
                
            res_2.append(t[i])
            
        if res_1 == res_2: return True
        
        return False