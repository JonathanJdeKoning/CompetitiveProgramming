tests = int(input())

for test in range(tests):
    total = 0
    num = [int(x) for x in input()]
    for c in range(len(num)-2, -1, -2):
        new = num[c]*2

        if new > 9:
            new = int(str(new)[0]) + int(str(new)[1])
        num[c] = new
    if sum(num) % 10 == 0:
        print("PASS")
    else:
        print("FAIL")