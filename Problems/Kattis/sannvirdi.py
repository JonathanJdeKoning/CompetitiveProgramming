N = int(input())
A = []
mp = {}
for _ in range(N):
    name, guess = input().split()
    guess = int(guess)
    A.append(guess)
    mp[guess] = name

A= sorted(A, reverse=True)


Q = int(input())
for _ in range(Q):
    K = int(input())
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low+high)//2
        val = A[mid]

        if val <= K:
            high = mid
        else:
            low = mid + 1
    if A[low] > K:
        print(":(")
    else:
        print(mp[A[low]])
