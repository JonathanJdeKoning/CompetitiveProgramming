s = []
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    data = input().split()
    op = data[0]

    if op == "push":
        s.append(data[1])
    elif op == "top":
        sys.stdout.write(str(s[-1])+"\n") if s else sys.stdout.write("-1\n")
    elif op =="size":
        sys.stdout.write(str(len(s)))
    elif op == "pop":
        sys.stdout.write(str(s.pop())+"\n") if s else sys.stdout.write("-1\n")
    elif op == "empty":
        sys.stdout.write("1\n") if not s else sys.stdout.write("0\n")
