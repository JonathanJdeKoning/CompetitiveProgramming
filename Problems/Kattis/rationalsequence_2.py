for _ in range(int(input())):
    ops = []
    case, number = input().split()
    num, den = number.split("/")
    num = int(num)
    den = int(den)

    while not (num == 1 and den == 1):
        if num > den:
            num -= den
            ops.append("R")
        else:
            den -= num
            ops.append("L")

    ops = ops[::-1]
    curr = 1

    for op in ops:
        if op == "L":
            curr*=2
        else:
            curr = curr*2+1
    print(case,curr)

