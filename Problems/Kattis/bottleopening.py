N = int(input())
K = int(input())
if K >= N: exit(print("impossible"))
curr = 2
for i in range(K):
    print(f"open {curr} using 1")
    curr += 1
    