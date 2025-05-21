n,b,p = list(map(int, input().replace(","," ").split()))
 
tb = 0
tp = n* p
while n != 1:
    competers = 2**(n.bit_length()-1)
    tb += b*competers + competers//2
 
    n = competers//2 + n-competers
 
print(tb, tp)