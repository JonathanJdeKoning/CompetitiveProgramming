for tc in range(int(input())):
    n,k = list(map(int, input().replace(","," ").split()))
    if n %2 ==0 or (k<=n and k%2==1):
        print("YES")
    else:
        print("NO")