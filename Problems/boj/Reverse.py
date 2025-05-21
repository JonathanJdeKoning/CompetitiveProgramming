N = int(input())
for _ in range(N):
    s, i, j = input().split()
    i = int(i)
    j = int(j)

    print(s[:i] +s[j:])