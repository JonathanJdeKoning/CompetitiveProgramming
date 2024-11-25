from itertools import permutations
ans = 0
x = ["0","1","2","3","4","5","6","7","8", "9"]
div = [2,3,5,7,11,13,17]
for perm in permutations(x):
    s = "".join(perm)
    for i in range(1,8):
        if int(s[i:i+3])%div[i-1] != 0:
            break
    else:
        ans +=int(s)

print(ans) 

