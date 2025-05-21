import sys
input = sys.stdin.readline

s = input().lstrip("0")
t = input().lstrip("0")

if len(s) < len(t):
    exit(print("<"))
elif len(s) > len(t):
    exit(print(">"))
else:
    for i in range(len(s)):
        if s[i] != t[i]:
            x, y = int(s[i]), int(t[i])
            if x < y:
                exit(print("<"))
            elif x > y:
                exit(print(">"))
print("=")