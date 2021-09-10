"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.total = ListNode(0)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        remainder = 0
        while l1 or l2 or remainder:
            num_sum = 0
            if l1:
                num_sum += l1.val
                l1 = l1.next
            if l2:
                num_sum += l2.val
                l2 = l2.next
            if remainder:
                num_sum += remainder
            self.total.next = ListNode(num_sum%10)
            self.total = self.total.next
            remainder = math.floor(num_sum/10)
        return self.total.next

solution = Solution()
solution.addTwoNumbers(
    l1=ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3))), 
    l2=ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
)
