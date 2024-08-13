for _ in range(int(input())):
    s = input()
    if s.count("a") == len(s):
        print("NO")
    else:
        print("YES")
        a = "a"+s
        b = s+"a"
        c = s[0]+"a"+s[1:]
        if a != a[::-1]:
            print(a)
        elif b != b[::-1]:
            print(b)
        elif c != c[::-1]:
            print(c)

