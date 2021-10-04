"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(nums) - 1
        
        found = False
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if nums[mid] == target:
                found = True
                start = mid
                end = mid - 1
                
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
                
        if not found: return [-1, -1]
        
        while start - 1 >= 0 and nums[start - 1] == target:
            start -=1
            
        while end + 1 <= len(nums) - 1 and nums[end + 1] == target:
            end += 1
            
        return [start, end]
            