branch = int(input())
tree = {}

while True:
    data = list(map(int, input().split()))
    if data[0] == -1:
        break

    for num in data[1:]:
        tree[num] = data[0]

output = [branch]
while True:
    try: 
        branch = tree[branch]
        output.append(branch)
    except:
        break
        
        
print(" ".join([str(x) for x in output]))
