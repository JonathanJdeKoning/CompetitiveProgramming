for _ in range(int(input())):
    N = int(input())
    uniq = set()
    mx = 0
    for _ in range(N):
        flake = int(input())
        if flake not in uniq:
            uniq.add(flake)
        else:
            mx = max(mx, len(uniq))
            uniq = set()
    print(mx)