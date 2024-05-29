n = int(input())

if n%2==1:
    b= bin(n)[2:]
    if b == b[::-1]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


