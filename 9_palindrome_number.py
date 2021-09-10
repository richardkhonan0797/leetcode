"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
"""

import math

def isPalindrome(x: int) -> bool:
    
    result = False
    if x < 0:
        return result
    
    container = []
    temp = x

    while temp > 0:
        num = temp % 10
        container.append(num)
        temp = math.floor(temp/10)
    
    reversed_num = 0

    for i, num in enumerate(container):
        reversed_num += num * 10**(len(container) - 1 - i)

    if reversed_num == x:
        result = True
    
    return result

print(isPalindrome(121))  # True
print(isPalindrome(-121)) # False
print(isPalindrome(10))   # False
print(isPalindrome(-101)) # False
