def solve():
    n = int(input())
    pigs, chicks = divmod(n,4)
    return(pigs+(chicks//2))





for _ in range(int(input())):
    print(solve())
