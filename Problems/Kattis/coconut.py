class Node:
    def __init__(self, val=None, next=None, hand=2):
        self.val = val
        self.next = next
        self.hand = hand

numRounds, numPlayers = map(int, input().split())

prev = Node(val=1)
start = prev
for i in range(2,numPlayers+1):
    new = Node(val=i)
    prev.next = new
    prev = new
prev.next = start
curr = start
if numRounds == 0: numRounds = 1
while True:
    if prev is curr:
        print(curr.val)
        break
    for _ in range(numRounds-1):
        prev = curr
        curr = curr.next

    if curr.hand ==2:
        curr.hand = 1
        newNode = Node(val=curr.val, next=curr.next, hand=1)
        curr.next= newNode
    elif curr.hand == 1:
        curr.hand = 0
        prev = curr
        curr = curr.next
    elif curr.hand == 0:
        prev.next = curr.next
        curr.next = None
        curr = prev.next





