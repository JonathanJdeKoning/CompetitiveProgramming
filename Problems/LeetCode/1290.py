# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        real = ""
        while head:
            real+= str(head.val)
            head = head.next
        return int(real,2) if real else 0
