input()
a = sum(map(int, input().split()))
b = sum(map(int, input().split()))
if a > b:
    print("Button 1")
elif b > a: print("Button 2")
else: print("Oh no")