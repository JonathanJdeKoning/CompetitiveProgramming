squares = set([x**2 for x in range(1,5*10**4) if x<=223])

def solve(n):
    if n in squares:
        return(1)

    for num in squares:
        if n-num in squares:
            return(2)

    for num1 in squares:
        for num2 in squares:
            if n - (num1+num2) in squares:
                return 3
    return 4


print(solve(int(input())))
