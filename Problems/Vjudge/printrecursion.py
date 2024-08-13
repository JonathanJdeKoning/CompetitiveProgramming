def solve(n):
    if n ==0: return
    print("I love Recursion")
    solve(n-1)
n = int(input())
solve(n)
