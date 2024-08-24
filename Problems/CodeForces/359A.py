R, C = map(int, input().split())

top = list(map(int, input().split()))
if 1 in top:
    exit(print(2))

for _ in range(R-2):
    row = list(map(int, input().split()))
    if row[0] == 1 or row[-1] == 1:
        exit(print(2))

bot = list(map(int, input().split()))
if 1 in bot:
    exit(print(2))
print(4)
