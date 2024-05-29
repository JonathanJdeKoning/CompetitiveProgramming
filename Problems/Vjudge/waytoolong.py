for _ in range(int(input())):
    s = input()
    if len(s) <= 10:
        print(s);continue

    print(f"{s[0]}{len(s)-2}{s[-1]}")
