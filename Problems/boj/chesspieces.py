pieces = list(map(int, input().split()))
ans = []

ans.append(1-pieces[0])
ans.append(1-pieces[1])
ans.append(2-pieces[2])
ans.append(2-pieces[3])
ans.append(2-pieces[4])
ans.append(8-pieces[5])
print(" ".join([str(x) for x in ans]))
