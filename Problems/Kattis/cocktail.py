
def solve():
    numpotions, time = map(int, input().split())
    potions = []
    chugtime = time
    for _ in range(numpotions):
        potions.append(int(input()))
    potions = sorted(potions, reverse=True)

    mx = chugtime + potions[0]
    for potion in potions:
        chugtime+= time
        length = chugtime+potion
        if length < mx:
            print("NO")
            return
    print("YES")

        
if __name__ == "__main__":
    solve()
