squares, move = map(int, input().split())
curr = 0
seen = set()
seen.add(curr)

arr = list(map(int, input().split()))
total = arr[curr]
while True:
    curr = (curr+move)%squares
    if curr in seen:
        break
    total += arr[curr]
    seen.add(curr)
print(total)
