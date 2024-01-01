str = input()

a = 1
b = 0
c = 0

for letter in str:
    if letter == "A":
        a, b = b,a
    elif letter == "B":
        b, c = c, b
    elif letter == "C":
        a, c = c, a

if a: print("1")
if b: print("2")
if c: print("3")