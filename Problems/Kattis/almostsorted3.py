def left(nums):
    run = True
    post = nums[0]
    for i, num in enumerate(nums[:-1]):
        if nums[i+1] < nums[i]:
            if not run: return "No"
        elif nums[i+1] > nums[i]:
            run = False
            begin = nums[i+1]
            if begin < post:
                return "No"
        

    return "Yes"

def mid(nums):
    prev = nums[0]
    lpost = None
    rpost = None
    start = None
    end = None
    running = False
    found = False
    for i, num in enumerate(nums[1:-1], start=1):
        next = nums[i+1]
        if num > next:
            if found: return "No"
            if not running:
                running = True
                lpost = prev
                start = num
        elif num < next:
            if running:
                found = True
                running = False
                rpost = next
                end = num
        prev = num
    if not rpost:
        rpost = float("inf")
        end = nums[-1]
    if end >= lpost and start <= rpost:
        return "Yes"
    else:
        return "No"

def right(nums):
    post = None
    prev = nums[0]
    running = False
    for i, num in enumerate(nums[1:-1], start=1):
        next = nums[i+1]
        if num > next:
            if not running:
                running = True
                post = prev
        elif next > num:
            if running: return "No"

        if num != next: prev = num
    if nums[-1] >= post: return "Yes"
    return "No"


def solve():
    nums = list(map(int, input().split()))
    if nums == sorted(nums): return ""
    if nums == sorted(nums, reverse=True): return ""
    print(nums) 

    start = nums[0]
    for num in nums[1:]:
        if num > start: break
        if num < start: return left(nums)
        start = num

    nums = nums[::-1]
    start = nums[0]
    for num in nums[1:]:
        if num < start: break
        if num > start: 
            nums = nums[::-1]
            return right(nums)
        start = num

    nums = nums[::-1]

    if nums[0] > nums[1]: return left(nums)
    if nums[-2] > nums[-1]: return right(nums)
    return mid(nums)
    
for _ in range(256):
    print(solve())
            
