for _ in range(int(input())):
    s = [int(x) for x in input()]

    if sum(s[:3]) == sum(s[3:]):
        print("YES")
        continue
    print("NO")
