while True:
    numnames = int(input())
    if numnames == 0 :
        break
    names = []
    for _ in range(numnames):
        names.append(input())
    print("\n".join(sorted(names, key=lambda x:(x[0],x[1]))))
    print()
