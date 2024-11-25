N = int(input())
for _ in range(N):
    elem = input()
    abb = input()
    for c in abb:
        if c not in elem:
            print("NO")
            break
    else:
        print("YES")