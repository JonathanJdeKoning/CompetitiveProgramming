N, K =  list(map(int, input().replace(","," ").split()))
items = []
for _ in range(N):
    M, V = list(map(int, input().replace(","," ").split()))
    
    items.append((V,M))
bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort(reverse=True)
items.sort(key=lambda x: (-x[0], x[1]))
print(items)
print(bags)
