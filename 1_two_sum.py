"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

def twoSum(nums: list[int], target: int) -> list[int]:

    values = dict()

    for i, elem in enumerate(nums):
        complement = target - elem
        
        if complement in values:
            return [values[complement], i]
        
        values[elem] = i

    return []
            
print(twoSum(nums=[2, 7, 11, 14], target=9)) # nums[0] + nums[1] == 9, return = [0, 1]
print(twoSum(nums=[3, 2, 4], target=6))      # nums[1] + nums[2] == 6, return = [1, 2]
print(twoSum(nums=[3, 3], target=6))         # nums[0] + nums[1] == 6, return = [0, 1]
