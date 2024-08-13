def solve():
    s = input()
    if len(s) <=2:
        return "NO"
    if s == "101":
        return "NO"
    if s.startswith("10") and s[2] != "0":
        return("YES")
    return "NO"

for _ in range(int(input())):
    print(solve())
