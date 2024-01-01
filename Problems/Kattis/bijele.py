k,q,r,b,n,p = list(map(int,input().split()))

out = ""

out += str(1 - k)+ " "
out += str(1 - q)+ " "
out += str(2 - r)+ " "
out += str(2 - b)+ " "
out += str(2 - n)+ " "
out += str(8 - p)
print(out)