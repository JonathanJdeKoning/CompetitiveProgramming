nums = list(map(int, input().split()))
    if len([x for x in nums if x%2==0]) >=2:
        return True
    else:
    return False
