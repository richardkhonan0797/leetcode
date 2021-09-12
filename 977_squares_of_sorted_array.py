"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

def sortedSquares(nums):
    
    start = 0
    end = len( nums ) - 1
    
    result = []
    
    while start <= end:
        sq_start = nums[start] ** 2
        sq_end = nums[end] ** 2
        
        if sq_start > sq_end:
            result.append(sq_start)
            start +=1
        else:
            result.append(sq_end)
            end -= 1
            
    return result[::-1]

print(sortedSquares([-4,-1,0,3,10])) # [0,1,9,16,100]
print(sortedSquares([-7,-3,2,3,11])) # [4,9,9,49,121]
