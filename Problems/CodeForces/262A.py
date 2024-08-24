n,k = map(int, input().split())
print(len([x for x in input().split() if x.count("4") + x.count("7") <= k]))
