bas, exp, N = map(int, input().split())
 
def pow(a, b, N):
    if not exp: return 1
    if b ==1: return a
    tmp = pow(a,b//2, N)%N
    res = (tmp*tmp)%N
    if b%2==1: res *= a
    return res%N
 
modulo = pow(bas,exp, N)%N
print(modulo);
