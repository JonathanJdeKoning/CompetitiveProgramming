apps, events= map(int, input().split())
phone = [0]*(apps+1)
unread = 0
for _ in range(events):
    op, app = map(int, input().split())
    if op == 1:
        phone[app] += 1
        unread += 1
    elif op == 2:
        unread += phone[app]
        phone[app] = 0
    elif op ==3:
        unread += min(phone[app], phone[app]-)

    
