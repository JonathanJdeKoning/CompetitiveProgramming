n = int(input())
s = input()

old = s
while True:
    s = old.replace("01", "")
    s = s.replace("10", "")

    if s == old:
        exit(print(len(s)))

    old = s
