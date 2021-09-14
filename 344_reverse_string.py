from typing import List

"""
Write a function that reverses a string. The input string is given as an array of characters s.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
        
    # 1st solution
    # start = 0
    # end = len(s) - 1
    
    # while start <= end:
    #     s[start], s[end] = s[end], s[start]
        
    #     start += 1
    #     end -= 1

    # 2nd solution
    # end = len(s) - 1
    # def recursive(s, index):
    #     if index <= end - index:
    #         s[index], s[end - index] = s[end - index], s[index]
    #         index += 1
    #         recursive(s, index)
    #     else:
    #         return
    
    # recursive(s, 0)


    # 3rd solution
    s[:] = s[::-1]
    
    print(s)

reverseString(["h","e","l","l","o"])
reverseString(["h","a","n","n","a","H"])
