# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_len(root):
            mylen = 0
            while root:
                root = root.next
                mylen += 1
            return mylen
        length = get_len(head)
        steps = length - n
        prev = head
        curr = head

        if n == 1 and not head.next:
            return
        if steps == 0:
            return head.next

        while steps != 0:
            steps -= 1
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr.next = None
        return head            
        
        

