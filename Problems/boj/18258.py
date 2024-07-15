qs = int(input())
from collections import deque
import sys
input = sys.stdin.readline
q = deque([])
for _ in range(qs):
    data = input().split()
    op = data[0]

    if op == "push":
        q.append(int(data[1]))
    elif op == "pop":
        if len(q) ==0 :
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(q.popleft())+"\n")
    elif op == "size":
        sys.stdout.write(str(len(q))+"\n")
    elif op == "empty":
        if len(q) == 0:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    elif op == "front":
        if len(q) == 0: sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(q[0])+"\n")
    elif op == "back":
        if len(q) == 0: sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(q[-1])+"\n")
