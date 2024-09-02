h,m = map(int, input().split(":"))

while True:
    m+=1
    if m == 60:
        m = 0 
        h+=1
        if h ==24:
            h = 0

    s = str(h).zfill(2)+str(m).zfill(2)
    if s == s[::-1]:
        print(s[:2]+":"+s[2:])
        break
