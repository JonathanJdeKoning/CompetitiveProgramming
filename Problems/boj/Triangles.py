while True:
    l = sorted(list(map(int, input().split())))
    if sum(l) == 0: break
    if l[0]+l[1] <= l[2]: print("Invalid"); continue

    if (c:= len(set(l))) == 1:
        print("Equilateral")
    elif c == 2:
        print("Isosceles")
    else:
        print("Scalene")
