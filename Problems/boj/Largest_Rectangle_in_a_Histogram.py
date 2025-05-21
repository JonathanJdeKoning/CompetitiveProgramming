while True:
    heights = list(map(int, input().replace(","," ").split()))
    if heights == [0]: break
    heights = heights[1:]
    stack = []
    heights.append(0)
    ans = max(heights)
    for i,h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            ans = max(ans, height*(i-index))
            start = index
        stack.append((start,h))
    print(ans)