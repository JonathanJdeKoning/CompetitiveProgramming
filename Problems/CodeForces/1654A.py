for tc in range(int(input())):
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    A.sort()
    print(A[-1] + A[-2])
    