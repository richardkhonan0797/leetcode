"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        visited = [[False] * cols for row in range(rows)]
        fresh_count = 0
        minutes = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append([row, col])
                    visited[row][col] = True
                elif grid[row][col] == 1:
                    fresh_count += 1
                else:
                    visited[row][col] = True
                    
        if not fresh_count:
            return 0
        
        dims = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
        while queue:
            cur_q_size = len(queue)
            minutes += 1
            
            for i in range(cur_q_size):
                cur_row = queue[i][0]
                cur_col = queue[i][1]

                for dim in dims:
                    row = cur_row + dim[0]
                    col = cur_col + dim[1]
                    
                    if (
                        row < 0 or row >= rows or 
                        col < 0 or col >= cols or 
                        visited[row][col]   
                    ):
                        continue
                        
                    queue.append([row, col])
                    visited[row][col] = True
                    fresh_count -= 1
                    
            queue = queue[cur_q_size:]
            
        if fresh_count:
            return -1

        return minutes - 1
                