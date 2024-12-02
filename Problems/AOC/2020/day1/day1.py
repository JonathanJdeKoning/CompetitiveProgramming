ans = set()
with open("day1.in", "r") as file:
    nums = [int(line.strip()) for line in file.readlines()]
    for numA in nums:
        for numB in nums:
            if numA + numB == 2020:
                ans.add(numA*numB)

    for a in nums:
        for b in nums:
            for c in nums:
                if a+b+c == 2020:
                    ans.add(a*b*c)
print(*sorted(ans))