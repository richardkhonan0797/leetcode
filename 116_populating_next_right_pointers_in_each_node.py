# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root or not root.left or not root.right:
            return root
        
        root.left.next = root.right
        
        if root.next:
            root.right.next = root.next.left
            
        return Node(val=root.val, left=self.connect(root.left), right=self.connect(root.right), next=root.next)