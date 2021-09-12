"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    needed_rotations =  k % len(nums)
    
    nums[:] = nums[len(nums) - needed_rotations:] + nums[:len(nums) - needed_rotations]
    print(nums)
            
rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3) # [5,6,7,1,2,3,4]
rotate(nums=[1, 2], k=5) # [2, 1]