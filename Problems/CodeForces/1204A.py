s = int(input(),2)
o = 0

c = 0
while True:
    if 4**c< s:
        o += 1
    else:
        break
    c+= 1

print(o)
