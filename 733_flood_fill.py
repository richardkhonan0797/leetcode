"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
"""

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        if image == None or image[sr][sc] == newColor:
            return image
        
        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image
    
    def fill(self, image, row, column, initial, newColor):

        if (
            row < 0 or row >= len(image) or 
            column < 0 or column >= len(image[0]) or 
            image[row][column] != initial
        ):
            return

        image[row][column] = newColor
        
        self.fill(image, row - 1, column, initial, newColor) # up
        self.fill(image, row + 1, column, initial, newColor) # down
        self.fill(image, row, column - 1, initial, newColor) # left
        self.fill(image, row, column + 1, initial, newColor) # right