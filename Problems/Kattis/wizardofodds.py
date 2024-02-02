n, k = list(map(int, input().split()))

count = 0
while True:

    if n == 1:
        if count <= k:
            print("Your wish is granted!")
            break
        else:
            print("You will become a flying monkey!")
            break
    
    if n%2 == 0:
        n/=2
    else:
        n = (n+1)/2
    count += 1

