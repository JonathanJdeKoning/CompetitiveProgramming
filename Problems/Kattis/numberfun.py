tests = int(input())

output = []

for i in range(tests):
    x,y,z = list(map(int, input().split()))

    result = "Impossible"
    if x+y ==z: result = "Possible"
    if x*y ==z: result = "Possible"
    if x-y ==z: result = "Possible"
    if y-x ==z: result = "Possible"
    if x/y ==z: result = "Possible"
    if y/x ==z: result = "Possible"

    output.append(result)

print("\n".join(output))