def solve():
    numX, numY, w = map(float, input().split())
    if int(numX + numY + w) == 0: return""
    xCuts = list(map(float, input().split()))
    yCuts = list(map(float, input().split()))
    half = w/2
    xChunks = []
    yChunks = []
    
    for cut in xCuts:
        xChunks.append([cut-half,cut+half])
    xChunks.sort()
    if xChunks[0][0] > 0: return "NO"
    if xChunks[-1][-1] < 75: return "NO"

    start = xChunks[0][1]
    for chunk in xChunks[1:]:
        if chunk[0] > start: return "NO"
        start = chunk[1]
    
    for cut in yCuts:
        yChunks.append([cut-half,cut+half])
    yChunks.sort()
    if yChunks[0][0] > 0: return "NO"
    if yChunks[-1][-1] < 100: return "NO"

    start = yChunks[0][1]
    for chunk in yChunks[1:]:
        if chunk[0] > start: return "NO"
        start = chunk[1]
    return "YES"

while True:
    res = solve()
    if res == "": break
    print(res)
