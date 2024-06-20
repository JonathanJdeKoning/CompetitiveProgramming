import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    data = input().split()

    op = data[0]
    if op == "add":
        s.add(data[1])
    elif op == "check":
        if data[1] in s:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    elif op == "remove":
        s.discard(data[1])
    elif op == "empty":
        s = set()
    elif op == "all":
        s = {"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"}
    elif op == "toggle":
        if data[1] in s:
            s.discard(data[1])
        else:
            s.add(data[1])

