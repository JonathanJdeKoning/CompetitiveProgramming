n = int(input())
nums = list(map(int, input().split()))
while True:
    sorted = True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            sorted = False
    if sorted:
        print(" ".join([str(x) for x in nums]))
        break
