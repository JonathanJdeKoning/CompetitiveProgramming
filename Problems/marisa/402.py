n = int(input())
k = 1
count = 0

while True:
    if k >= n:
        exit(print(count))
    count += 1
    k*=2
    
