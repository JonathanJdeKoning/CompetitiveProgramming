for _ in range(int(input())):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i,num in enumerate(A):
        if num not in B: continue
        if B.count(num) != 1: print("YES"); break
        if B[i] != num: print("YES"); break
    else:
        print("NO")

    