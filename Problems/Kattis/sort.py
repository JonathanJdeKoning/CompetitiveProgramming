n, c = map(int, input().split())
nums = list(map(int, input().split()))
print(" ".join([str(x) for x in sorted(nums, key=lambda x:(nums.count(x),-nums.index(x)), reverse=True)]))
