n = int(input())

for i in range(n+1):
    nums = [str(x) for x in list(range(i+1)) + list(range(i-1,-1,-1))]
    print(" "*((n*2)-(i*2)),end = "")
    print(" ".join(nums))
for i in range(n-1,-1,-1):
    nums = [str(x) for x in list(range(i+1)) + list(range(i-1,-1,-1))]
    print(" "*((n*2)-(i*2)),end = "")
    print(" ".join(nums))
