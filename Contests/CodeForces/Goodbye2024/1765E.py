from math import ceil
def solve():
    cost, silver, gold = list(map(int, input().replace(","," ").split()))
    if silver > gold: return 1
    return(ceil(cost/silver))

for tc in range(int(input())):
    print(solve())
