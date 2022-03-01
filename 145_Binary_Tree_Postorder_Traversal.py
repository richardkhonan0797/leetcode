# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        else:
            if not root.left and not root.right:
                self.res += [root.val]
            else:
                self.postorderTraversal(root.left)
                self.postorderTraversal(root.right)
                self.res += [root.val]
            
        return self.res
            
