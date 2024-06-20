k = 15
n = 15
apt = []
base = [i for i in range(1,k+1)]
apt.append(base)
for i in range(1,k+1):
    new = []
    for j in range(1,n+1):
        new.append(sum(apt[i-1][:j]))
    apt.append(new)

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(apt[k][n-1])
