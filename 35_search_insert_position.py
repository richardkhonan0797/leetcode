"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
"""

def searchInsert(nums, target):
    
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        middle = start + (end - start) // 2
        
        if start == end:
            if target > nums[start]:
                return start + 1
            else:
                return start
        elif nums[middle] == target:
            return middle
        elif nums[middle] < target:
            start = middle + 1
        else:
            end = middle
            
print(searchInsert(nums=[1,3,5,6], target=5)) # 2
print(searchInsert(nums=[1,3,5,6], target=2)) # 1
print(searchInsert(nums=[1,3,5,6], target=7)) # 4
print(searchInsert(nums=[1,3,5,6], target=0)) # 0
print(searchInsert(nums=[1], target=0))       # 0