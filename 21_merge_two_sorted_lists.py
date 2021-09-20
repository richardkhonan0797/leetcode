"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        
        if l1 and l2:
            if l1.val <= l2.val:
                return ListNode(l1.val, next=self.mergeTwoLists(l1.next, l2))
            else:
                return ListNode(l2.val, next=self.mergeTwoLists(l1, l2.next))
        elif l1:
            return ListNode(l1.val, next=self.mergeTwoLists(l1.next, None))
        elif l2:
            return ListNode(l2.val, next=self.mergeTwoLists(l2.next, None))
