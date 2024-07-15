def solve(n):
    if n < 10: return n
    digs = len(str(n))
    total = 0
    total += 10**(digs-1)-1
    return(total)

print(solve(int(input())))
