from collections import deque
while True:
    try:
        numnums = int(input())
        my_q = deque([])
        my_s = []
        my_p = []
        q = True
        s = True
        p = True
        for i in range(numnums):
            op, val = map(int, input().split())
            if op == 1:
                my_s.append(val)
                my_q.append(val)
                my_p.append(val)
            else:
                try:
                    s_val = my_s.pop()
                    q_val = my_q.popleft()
                    p_val = max(my_p)
                    my_p.remove(p_val)
                except:
                    q = False
                    s = False
                    p = False
                
                if val != s_val:
                    s = False
                if val != q_val:
                    q = False
                if val != p_val:
                    p = False
        if len([x for x in [q,s,p] if x]) > 1:
            print("not sure")
            continue
        if not s and not q and not p:
            print("impossible")
            continue
        if s: print("stack")
        if q: print("queue")
        if p: print("priority queue")
        
            
        
    except EOFError:
        break
