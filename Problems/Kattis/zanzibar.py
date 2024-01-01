tests = int(input())

for i in range(tests):
    imports = 0
    hist = list(map(int, input().split()))
    
    curr = hist[0]
    imports = 0
    for item in hist[1:]:
        if item > curr*2:
            imports += item-(curr*2)
        curr = item
    print(imports)