
import sys
input = sys.stdin.readline
N = int(input())
strings = [input().strip() for _ in range(N)]

for _ in range(N-1):
    i,j = map(int, input().split())
    strings[i-1] = "".join([strings[i-1], strings[j-1]])
    strings[j-1] = ""
for s in strings:
    if s:
        exit(print(s))
