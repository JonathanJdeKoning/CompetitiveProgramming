
m = {"1":3,"2":6,"3":9,"4":2,"5":5,"6":8,"7":1,"8":4,"9":7,"0":10}
for _ in range(int(input())):
    N = int(input())
    
    last = str(N)[-1]
    ans = m[last]
    if N < ans*7:
        print(-1)
    else:
        print(ans)

