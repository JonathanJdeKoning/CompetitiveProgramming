for tc in range(int(input())):
    n,k,x = list(map(int, input().replace(","," ").split()))
    if x != 1:
        print("YES")
        print(n)
        print(" ".join(map(str, [1]*n)))
        continue
    if x == 1 and k == 1:
        print("NO")
        continue
    if x == 1 and k == 2:
        if n%2 == 0:
            print("YES")
            print(n//2)
            print(" ".join(map(str, [2]*(n//2))))
            continue
        else:
            print("NO")
            continue
    if x == 1 and k >= 3:
        print("YES")
        if n%2 == 0:
            print(n//2)
            print(" ".join(map(str, [2]*(n//2))))
        else:
            z = n//2
            A = [2]*(z-1)
            A.append(3)
            print(z)
            print(" ".join(map(str, A)))
            continue