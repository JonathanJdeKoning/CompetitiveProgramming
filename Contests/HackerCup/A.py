for i in range(1, int(input())+1):
    N, K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(int(input()))

    mn = min(A)

    wheels = len(A) - 1
    total = mn*abs(((wheels*2)-1))
    if total <= K:
        print(f"Case #{i}: YES")
    else:
        print(f"Case #{i}: NO")

