# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        allem = []
        for l in [list1, list2]:
            while l:
                allem.append(l.val)
                l = l.next
        allem.sort()
        if len(allem) == 0: return None
        if len([list1, list2]) == 0: return None


        new = ListNode(val=allem[0])
        dummy = ListNode(0, next=new)
        for i in allem[1:]:
            node = ListNode(i)
            new.next = node
            new = node
        return dummy.next

