"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
Example 4:

Input: n = 4
Output: true
Example 5:

Input: n = 5
Output: false
"""

import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
#         loop 1
#         num = 1
    
#         while(num < n):
#             num *= 2
            
#         if num == n:
#             return True

#         return False

#         loop 2
        
#         if n == 0: return False
#         if n == 1 or n == 2: return True
        
#         while n > 1:
#             n = n/2
            
#             if n == 1:
#                 return True
            
#             if n % 2 != 0:
#                 return False
        
#         recursion
#         if n == 0: return False
#         if n == 1 or n == 2: return True
        
#         n = n/2
        
#         if n % 2 == 0:
#             return self.isPowerOfTwo(n)
#         else:
#             return False

#         shift right (1100 -> 0110 -> 0011 = False, 100 -> 010 -> 001 = True)
        while n > 1 and n&1 == 0:
            n >>= 1
            
        return True if n == 1 else False

#         """
#         Log2(n):
#         Ex: n = 16
#         log2(16) = 4, ceil(4) == floor(4) = True
#         Ex: n = 12
#         log2(12) = 3.58, ceil(3.58) != floor(3.58) = False
#         """
#         if n <= 0: return False
        
#         log = math.log2(n)
#         return True if math.ceil(log) == math.floor(log) else False