for _ in range(int(input())):
    x = input()
    s = input()
    if "B" in s:
        first = s.find("B")
        last = len(s) - s[::-1].find("B") - 1
        print(str(1+(last - first)))
    else:print("0")
