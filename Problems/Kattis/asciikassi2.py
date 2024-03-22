n = int(input())

startspaces = n+1
print(" "*startspaces,end="")
print("x")

for i in range(n,0,-1):
    print(" "*i,end="")
    print("/",end="")
    midspace = ((n-i)*2)+1
    print(" "*midspace,end="")
    print("\\")

print(f"x{' '*((n*2)+1)}x")

for i in range(1,n+1):
    print(" "*i,end="")
    print("\\",end="")
    midspace = ((n-i)*2)+1
    print(" "*midspace,end="")
    print("/")

endspaces = n+1
print(" "*endspaces,end="")
print("x")


