n = int(input())
m,s = divmod(n, 60)

h,m = divmod(m,60)

print(f"{h} : {m} : {s}")
