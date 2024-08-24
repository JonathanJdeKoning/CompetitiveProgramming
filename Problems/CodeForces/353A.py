n =int(input())
m = int(input())
if n==m:
    exit(print("YES\n0"))
curr = n
c = 0



while True:
    curr*=n
    c+=1

    if curr ==m:
        print("YES")
        print(c)
        break
    elif curr > m:
        print("NO")
        break
