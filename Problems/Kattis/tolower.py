problems, tests = list(map(int, input().split()))
total = 0
for p in range(problems):
    want = []
    have = []
    for test in range(tests):
        string = input()
        want.append(string.lower())
        have.append(string[0].lower()+string[1:])
    if want == have:
        total += 1
print(total)
