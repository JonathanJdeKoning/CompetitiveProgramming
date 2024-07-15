class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

n, k = map(int, input().split())

prev = Node(val=1)
start = prev
for i in range(2,n+1):
    new = Node(val=i)
    prev.next = new
    prev = new
prev.next = start
curr = start
out = []
while True:
    if prev is curr:
        out.append(curr.val)
        break
    for _ in range(k-1):
        prev = curr
        curr = curr.next
    out.append(curr.val)
    prev.next = curr.next
    curr.next = None
    curr = prev.next
print("<" + str(out)[1:-1] + ">")





