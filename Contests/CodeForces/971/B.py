def solve():
    n = int(input())
    out = []

    for _ in range(n):
        row = input()
        out.append(row.index("#")+1)

    return " ".join(map(str, out[::-1]))


for _ in range(int(input())):
    print(solve())
