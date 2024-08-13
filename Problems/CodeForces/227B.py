import sys
input = sys.stdin.readline
vas = 0
pet = 0

ans = {}


n = int(input())
nums = map(int, input().split())
k = int(input())
qs = map(int, input().split())

for i, num in enumerate(nums, start=1):
    ans[num] = (i, (n-i)+1)

for q in qs:
    v,p = ans[q]
    vas += v
    pet += p

sys.stdout.write(f"{vas} {pet}\n")



