n = int(input())
glob = input()
pref, suff = glob.split("*")
for _ in range(n):
    s = input()
    if s.startswith(pref) and s.endswith(suff) and len(s) >= len(glob)-1:
        print("DA")
    else:
        print("NE")
    
