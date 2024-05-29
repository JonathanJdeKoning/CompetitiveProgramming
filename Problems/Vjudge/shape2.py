n = int(input())
for i in range(n-1,-1,-1):
    print(" "*i, end="")
    opp = n-i
    print("*"*(opp+opp-1))
