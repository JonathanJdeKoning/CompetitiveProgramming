nums = int(input())

numlist = list(map(int, input().split()))

alice = 0
bob = 0
while len(numlist) != 0:
    maxi = max(numlist)
    alice += max(numlist)
    numlist.remove(maxi)
    if len(numlist) == 0:
        break
    maxi = max(numlist)
    bob += max(numlist)
    numlist.remove(maxi)

print(f"{alice} {bob}")