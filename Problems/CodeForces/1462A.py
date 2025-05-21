for tc in range(int(input())):
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    mid = len(A) // 2
    out = []
    l = 0
    r = len(A) - 1

    while l<= r:
        if l == r:
            out.append(A[l])
        else:
            out.append(A[l])
            out.append(A[r])
        l += 1
        r -= 1
    print(" ".join(map(str, out )))
    