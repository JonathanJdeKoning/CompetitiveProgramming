import re
ans2 = 0
pat = re.compile(r"mul\((\d+),(\d+)\)")
with open("day3.in", "r") as file:
    s = "".join([x.strip() for x in file.readlines()])

print(sum(int(match.group(1)) * int(match.group(2)) for match in pat.finditer(s)))
done = False
while not done:
    if "don't()" not in s: done = True
    else: t, s = s[s.index("don't()"):], s[:s.index("don't()")]

    ans2 += sum([int(match.group(1)) * int(match.group(2)) for match in pat.finditer(s)])
    if "do()" not in t: break
    s = t[t.index("do()"):]

print(ans2)