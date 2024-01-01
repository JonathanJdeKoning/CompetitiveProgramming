n = int(input())

nums = []
while True:
    nums.append(int(n))
    if n == 1:
        break
    if n%2==0:
        n/=2
    else:
        n*=3
        n+=1
print(" ".join(list(map(str, nums))))
