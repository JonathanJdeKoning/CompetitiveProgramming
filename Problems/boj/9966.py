n = int(input())
m = int(input())

def rot(num):
    s = str(num)
    for bad in "23457":
        if bad in s: return "."
    
    new = []

    for c in s:
        if c == "6":
            new.append("9")
        elif c == "9":
            new.append("6")
        else:
            new.append(c)
    return int("".join(new)[::-1])

ans = 0
for num in range(n,m +1):
    if num == rot(num):
        ans += 1
print(ans)
