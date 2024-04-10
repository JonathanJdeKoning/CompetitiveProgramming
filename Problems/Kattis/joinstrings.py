import sys
input = sys.stdin.readline
numstrings = int(input())
strings = [input()[:-1] for x in range(numstrings)]
for _ in range(numstrings-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    strings[a] += strings[b]
    strings[b] = ""
sys.stdout.write([x for x in strings if x][0])
