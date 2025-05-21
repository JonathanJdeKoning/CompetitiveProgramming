a = []
for i in range(1,10):
    for j in range(1,5):
        a.append(str(i)*j)
for tc in range(int(input())):
    n = input()
    ans = 0
    for c in a:
        ans += len(c)
        if c == n:
            print(ans)
            break         
    