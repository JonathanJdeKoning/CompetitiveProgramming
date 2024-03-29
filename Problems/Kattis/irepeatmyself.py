for _ in range(int(input())):
    s = input()
    l= len(s)
    for i in range(l):
        if l%(i+1) != 0: continue
        
        if s[:i+1]*(l//(i+1)) == s:
            print(i+1)
            break
