"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example 1:


Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        merged = self.merge(root1, root2)
        
        return merged
    
    def merge(self, root1, root2):
        if not root1 and not root2:
            return None
        
        total = 0
        
        if root1:
            total += root1.val
            
        if root2:
            total += root2.val
            
        if not root1 and not root2:
            total = None
            
        r1_left = root1.left if root1 else None
        r1_right = root1.right if root1 else None
        r2_left = root2.left if root2 else None
        r2_right = root2.right if root2 else None
        
        return TreeNode(val=total, left=self.merge(r1_left, r2_left), right=self.merge(r1_right, r2_right))
        