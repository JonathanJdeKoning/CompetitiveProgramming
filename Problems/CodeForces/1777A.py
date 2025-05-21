for tc in range(int(input())):
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    ans = 0
    while True:
        done = True
        new = []
        curr = 0
        while curr <= len(A)-1:
            if curr == len(A) - 1:
                new.append(A[curr])

            elif A[curr]%2 == A[curr+1]%2:
                new.append(A[curr]*A[curr+1])
                curr += 1
                done = False
                ans += 1
            else:
                new.append(A[curr])
            curr += 1
        if done:
            break
        A = new
    print(ans)








