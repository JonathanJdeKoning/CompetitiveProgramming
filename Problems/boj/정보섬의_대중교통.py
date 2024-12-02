n,a,b = list(map(int, input().split()))
if n > b:
    exit(print("Bus"))

if n + (b-n) < a:
    print("Subway")
elif a < n + (b-n):
    print("Bus")
else:
    print("Anything")