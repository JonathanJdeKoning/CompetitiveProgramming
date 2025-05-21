X, Y = list(map(int, input().replace(","," ").split()))

curr = X
val = 1
dist = 0
while True:
    dist += abs(val)
    curr = X+val
    if (X<=Y<=curr) or (curr<=Y<=X):
        exit(print(dist - abs(Y-curr)))
    val *= -2
    dist += abs(val//2)