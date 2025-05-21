from math import ceil
K, N = list(map(int, input().replace(","," ").split()))
for _ in range(N):
    S, T, R = list(map(int, input().replace(","," ").split()))
    read = 0
    minutes = 0
    while True:
        read += S*T
        minutes += T

        if read >= K:
            minutes -= (read-K)/S
            break
        minutes += R
    print(ceil(minutes))
