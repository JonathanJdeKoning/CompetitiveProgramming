a,b,c,x,y,z=list(map(int,input().split()))+list(map(int, input().split()));m=min(a/x,b/y,c/z);print(a-m*x,b-m*y,c-m*z)
