
def findNthDigit(p, q, N) : 
    while (N > 0) :
        N -= 1; 
        p *= 10; 
        res = p // q; 
        p %= q; 
 
    return res; 


a,b,c = map(int, input().split())
print(findNthDigit(a,b,c))
