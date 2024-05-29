nums =set()
n,m = map(int, input().split())
for _ in range(n):
    nums.update(set(input().split()))
x = input()
if x in nums:
    print("will not take number")
else:
    print("will take number")
