from collections import deque
for _ in range(int(input())):
    input()
    nums = deque(sorted(list(map(int, input().split()))))
    out = []
    top = True
    while nums:
        if top:
            out.append(nums.pop())
        else:
            out.append(nums.popleft())
        top = not top


    print(" ".join([str(x) for x in out[::-1]]))
