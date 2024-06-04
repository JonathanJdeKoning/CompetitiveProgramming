import sys
input = sys.stdin.readline
    
for _ in range(int(input())):
    a,b = map(int, input().split())
    sys.stdout.write(str(a*b))
    sys.stdout.write("\n")
