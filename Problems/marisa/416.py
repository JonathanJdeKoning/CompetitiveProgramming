s = int(input())

m,s = divmod(s, 60)
h,m = divmod(m,60)
print(h,m,s)
