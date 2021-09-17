"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_len = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                cur_len = self.calcArea(grid, row, col)

                if cur_len > max_len:
                    max_len = cur_len

        return max_len

    def calcArea(self, grid, row, col):
        if (
            row < 0 or row >= len(grid) or
            col < 0 or col >= len(grid[0]) or
            grid[row][col] != 1
        ):
            return 0 
        
        grid[row][col] = 0
        
        up = self.calcArea(grid, row - 1, col)
        down = self.calcArea(grid, row + 1, col)
        left = self.calcArea(grid, row, col - 1)
        right = self.calcArea(grid, row, col + 1)
        
        return up + down + left + right + 1
        