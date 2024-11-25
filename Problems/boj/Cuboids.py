while True:
    l,w,h,v = map(int, input().split())
    if sum([l,w,h,v]) == 0: break
    a = l*w*h
    if v != 0:
        g = [x for x in [l,w,h] if x]
        a = v//(g[0]*g[1])
    
    out = [l,w,h,v]
    for i, val in enumerate(out):
        if val == 0: out[i] = a
    print(*out)