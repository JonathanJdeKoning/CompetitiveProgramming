n = float(input())
start = 1
while True:
    n /= start
    if n == 1:
        print(start)
        break
    start += 1    
