def solve():
    good = set()
    for i in range(1,int(input())+1):
        line = input()
        if line.startswith("->"):
            good.add(line[3:])
            continue

        data = line.split()
        for axiom in data[:-2]:
            if axiom not in good:
                return i
        good.add(data[-1])
    return "correct"
print(solve())
