def solve(n):
    if n%2==1: return "Either"
    return "Even" if n%4==0 else "Odd"
print(solve(int(input())))
