cows = {
    "Bessie": 0,
    "Maggie": 0,
    "Elsie": 0,
    "Daisy": 0,
    "Gertie": 0,
    "Annabelle": 0,
    "Henrietta": 0
}

N = int(input())
for _ in range(N):
    cow, milk = input().split()
    cows[cow] += int(milk)

M = min(cows.values())

other = sorted([x for x in cows.values() if x > M])
if not other or (len(other)> 1 and other[0] == other[1]):
    print("Tie")
else:
    winner = other[0]

    for k, v in cows.items():
        if v == winner:
            exit(print(k))
