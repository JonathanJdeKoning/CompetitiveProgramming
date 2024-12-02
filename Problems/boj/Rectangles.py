rectW,rectH,p = list(map(int, input().split()))
ans = 0
for width in range(1,rectW+1):
    for height in range(1, rectH+1):
        if 2*width + 2*height < p: continue
        ans += ((rectW-width)+1) * (1+(rectH - height))
print(ans)