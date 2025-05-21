N = int(input())
A = 0
for _ in range(N):
    input()
    A += int(input())

if A == 0:
    print("Lagom")
elif A < 0 :
    print("Nekad")
else:
    print("Usch, vinst")