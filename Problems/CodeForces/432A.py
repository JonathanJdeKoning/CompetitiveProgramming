n,k = map(int, input().split())

n = list(map(int, input().split()))

print(len([x for x in n if x <= 5-k])//3)
