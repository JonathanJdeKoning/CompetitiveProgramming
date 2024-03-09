mem = [0,1]
total = 0
idx = 2
while True:
    num = mem[idx-1]+ mem[idx-2]
    if num > 4000000: break
    mem.append(num)
    idx += 1
    if num%2 == 0:
        total += num
print(total)

