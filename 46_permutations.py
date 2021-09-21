"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""

from typing import List


class Solution:
    def __init__(self):
        self.res = []
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.backtrack(nums, [])

        return self.res
        
    def backtrack(self, nums, path):

        if not nums:
            self.res.append(path)
            print("nums: ", nums)
            print("path: ", path)
            print("res: ", self.res)

        for i in range(len(nums)):
            print("nums: ", nums)
            print("path: ", path)
            self.backtrack(nums[:i]+nums[i+1:], path+[nums[i]])

solution = Solution()
print(solution.permute([1, 2, 3]))
