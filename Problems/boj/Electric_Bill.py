f, s = list(map(int, input().split()))
N = int(input())
for _ in range(N):
    use = int(input())
    if use <= 1000: print(use, f*use)
    else:
        print(use, f*1000 + s*(use-1000))