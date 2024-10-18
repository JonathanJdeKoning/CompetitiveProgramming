
def solve():
    a,b = list(map(int, input().split()))

    if (a+b)%3!=0: return "NO"
    if  min(a,b) < max(a,b)/2 : return "NO"
    return "YES"


for _ in range(int(input())):
    print(solve())    