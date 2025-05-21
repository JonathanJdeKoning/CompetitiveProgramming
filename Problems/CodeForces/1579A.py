for tc in range(int(input())):
    s = input()
    if s.count("B") == s.count("A") + s.count("C"):
        print("YES")
    else:
        print("NO")
    