def solve():
    data = input().split()
    if len(data) == 1:
        n = int(data[0])
        return (2**(n+1))-1
    n = int(data[0])
    s = data[1]
    root = (2**(n+1))-1
    total = 0
    start = 1
    par = "G"
    for c in s:
        if par == "G":
            if c == "R":
                start*=2
            elif c == "L":
                start = start*2-1
                par = "P"
        elif par == "P":
            if c == "L":
                start*=2
            elif c == "R":
                start =start*2+1
                par = "G"
        total += start
    return(root-total)
print(solve())

