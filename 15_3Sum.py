"""

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

Steps:
1. Sort the nums
2. Loop nums and find sum of num i + left num (i + 1) + right num (length of num - 1)
3. If equals 0 append to result, else if sum > 0 shift right - 1, else if sum < 0 shift left +  1

[-4, -1, -1, 0, 1, 2]
  ^   ^            ^
  i   l            r
"""

from typing import List


class Solution:
    def __init__(self):
        self.result = []
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                sum_val = nums[i] + nums[l] + nums[r]
                
                if sum_val > 0:
                    r -= 1
                elif sum_val < 0:
                    l += 1
                else:
                    self.result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return self.result