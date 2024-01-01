for i in range(int(input())):
    pieces = int(input())

    a = [(int(x[:-1]), x[-1]) for x in input().split()]
    red = [x for x in a if x[1] == "R"]
    blue = [x for x in a if x[1]== "B"]
    mini = min(len(red), len(blue))

    red = sorted(red, key=lambda x:x[0], reverse=True)[:mini]
    blue = sorted(blue, key=lambda x:x[0], reverse=True)[:mini]

    total = 0
    for piece in red:
        total += (piece[0]-1)
    for piece in blue:
        total += (piece[0]-1)
    print(f"Case #{i+1}: {total}")
