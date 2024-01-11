# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        while True:
            if not l1:
                break
            num1.append(l1.val)
            l1 = l1.next

        while True:
            if not l2:
                break
            num2.append(l2.val)
            l2 = l2.next
    
        num1 = int("".join([str(x) for x in num1]))
        num2 = int("".join([str(x) for x in num2]))
        res =str(num1+num2)
        ans = [int(x) for x in res][::-1]
        root = ListNode(ans[0])
        curr = root
        for i in ans[1:]:
            new = ListNode(i)
            curr.next = new
            curr = new
        return root


