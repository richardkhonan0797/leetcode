"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        nums_1 = nums[:-1]
        nums_2 = nums[1:]
        
        dp_1 = [nums_1[0], max(nums_1[0], nums_1[1])]
        dp_2 = [nums_2[0], max(nums_2[0], nums_2[1])]
        
        for i in range(2, len(nums_1)):
            dp_1.append(max(nums_1[i] + dp_1[i - 2], dp_1[i - 1]))
            
        for j in range(2, len(nums_2)):
            dp_2.append(max(nums_2[j] + dp_2[j - 2], dp_2[j - 1]))
            
        return max(dp_1[-1], dp_2[-1])