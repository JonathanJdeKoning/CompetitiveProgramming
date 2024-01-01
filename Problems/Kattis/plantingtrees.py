n = int(input())
trees = sorted(list(map(int, input().split())), reverse=True)
maxi = -1

for idx, tree in enumerate(trees):
    calc = ((tree + 1)+ idx)+1
    if calc > maxi:
        maxi = calc
print(maxi)
