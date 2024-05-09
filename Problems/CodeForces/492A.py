n = int(input())

blocks = 0
i = 0
layer = 0
while True:
    layer += i
    blocks += layer
    if blocks == n:
        print(i)
        break
    if blocks > n:
        print(i-1)
        break
    i+=1
