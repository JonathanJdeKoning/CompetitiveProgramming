a = [0]*10001
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a[int(input())] += 1
for i,num in enumerate(a[1:], start=1):
    if num == 0: continue
    for j in range(num):
        sys.stdout.write(str(i)+"\n")
