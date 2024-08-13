def sum_arr(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_arr(arr[1:])
for i in range(int(input())):
    nums = list(map(int, input().split()))
    nums = nums[1:]
    print(f"Case {i+1}: {sum_arr(nums)}")


