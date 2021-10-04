"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if len(matrix) == 0: return False
        
        tgt_row = -1
        
        for i, row in enumerate(matrix):
            if target >= row[0] and target <= row[len(row) - 1]:
                tgt_row = i
                break
                
        if tgt_row < 0: return False
        
        nums = matrix[tgt_row]
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False
                