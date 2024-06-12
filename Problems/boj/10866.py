from collections import deque
import sys
input = sys.stdin.readline
q = deque()
for _ in range(int(input())):
    data = input().split()
    op = data[0]

    if op == "front":
        if not q: sys.stdout.write("-1\n")
        else: sys.stdout.write(q[-1]+"\n")
    elif op == "back":
        if not q: sys.stdout.write("-1\n")
        else: sys.stdout.write(q[0]+"\n")
    elif op == "size": sys.stdout.write(str(len(q))+"\n")
    elif op == "empty": sys.stdout.write("1\n") if not q else sys.stdout.write("0\n")
    elif op == "push_back": q.appendleft(data[1])
    elif op == "push_front": q.append(data[1])

    elif op == "pop_back":
        if not q: sys.stdout.write("-1\n")
        else: sys.stdout.write(q.popleft()+"\n")
    elif op == "pop_front":
        if not q: sys.stdout.write("-1\n")
        else: sys.stdout.write(q.pop()+"\n")
