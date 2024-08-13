n = int(input())
def nto1(n):
    if n == 1:print("1", end="");return
    print(str(n) + " ",end="")
    nto1(n-1)

nto1(n)
