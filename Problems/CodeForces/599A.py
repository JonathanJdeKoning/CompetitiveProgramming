a,b,c = map(int, input().split())

i = a+b+b+a
j = c+b+a
k = a+c+c+a
l = b+c+c+b
print(min(i,j,k,l))



