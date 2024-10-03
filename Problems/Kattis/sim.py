class ListNode:
    def __init__(self, val="", next=None):
        self.val = val
        self.next = next


for _ in range(int(input())):
    s = input()
    end = ListNode()
    curr = ListNode(next=end)
    home = ListNode(next=curr)

    for c in s:
        if c == "]":

        elif c == "[":
        elif c == "<":
            
        else:
            new = ListNode(val = c, next = curr.next)
            curr.next = new
            curr = new


