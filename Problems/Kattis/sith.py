name = input()

a = int(input())
b = int(input())
res = int(input())

ans = a-b

if res < 0:
    print("JEDI")

if res > 0 and ans < 0:
    print("SITH")

if res > 0 and ans > 0:
    print("VEIT EKKI")