"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:


Input: mat = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
Output: [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
Example 2:


Input: mat = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
]
Output: [
    [0,0,0],
    [0,1,0],
    [1,2,1]
]
"""

from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        cols = len(mat[0])
        queue = []
        visited = [[False] * cols for row in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append([row, col])
                    visited[row][col] = True
        
        dimensions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while queue:
            curr_q_size = len(queue)
            
            for q in range(curr_q_size):
                curr_row = queue[q][0]
                curr_col = queue[q][1]
                
                for dim in dimensions:
                    row = curr_row + dim[0]
                    col = curr_col + dim[1]
                    
                    if row < 0 or row >= rows or  col < 0 or col >= cols or visited[row][col]:
                        continue
                    
                    queue.append([row, col])
                    visited[row][col] = True
                    
                    mat[row][col] = mat[curr_row][curr_col] + 1
            
            queue = queue[curr_q_size:]
            
        return mat
