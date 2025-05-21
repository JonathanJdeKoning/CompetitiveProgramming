N = int(input())
s = input()
A = 0
H = 0

a = 0
h = 0
for c in s:
    if c == "A": a += 1
    else:
        h += 1

    if a == 3:
        A += 1
        a =0 
        h = 0
    if h == 3:
        H += 1
        h = 0
        a = 0
    if A == N:
        exit(print("Hannes"))
    if H == N:
        exit(print("Arnar"))
