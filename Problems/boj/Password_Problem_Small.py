for tc in range(int(input())):
    K, N = list(map(int, input().replace(","," ").split()))
    A = list(map(float, input().split()))
    PP = []
    P = []
    R = []
    for i in range(1<<len(A)):
        r = 0 
        a = []
        for j in range(len(A)):
            if (i & (1 << j)):
                a.append(1)
            else:
                a.append(0)
                r = j+1
        a = a[::-1]
        #print(a)
        p = 1
        for l, k in enumerate(a):
            if k:
                p*= A[l]
            else:
                p*= 1-A[l]
        R.append(r)
        P.append(p)
    PP.append(R)
    PP.append(P)
    PP.append([N+2]*len(PP[0]))
    PP.append([N-K + 2 + N]* (len(PP[0])-1) + [(N-K) + 1])
    
    for bs in range(1, K+1):
        B = []
        for r in PP[0]:
            if r<= bs:
                B.append(bs + 1 + (N-(K-bs)))
            else:
                B.append(bs + (N-(K-bs)) + 1 + N + 1)
        PP.append(B)
    #for row in PP:
        #print(row)
    PP = PP[1:]
    exp = []
    for row in PP[1:]:
        e = 0
        for j, k in enumerate(row):
            e += k*PP[0][j]
        exp.append(e)
    #print(exp)
    #print()
    print(f"Case #{tc+1}: {min(exp)}")


        
                  
    