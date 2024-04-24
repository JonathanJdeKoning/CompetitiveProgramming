def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    
    good = True
    found = False
    running = False
    start = nums[0]
    left = None
    right = None
    for num in nums[1:]:
        if num > start:
            if running:
                found = True
                running = False
                right = start
        elif num < start:
            if found: return "No"
            running = True
            left = start
        start = num
    return "Yes"


print(solve())
            
