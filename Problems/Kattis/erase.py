dels = int(input())

orig = input()

new = ""
for c in orig:
    if c == "1":
        new += "0"
    else:
        new+= "1"

tryme = input()

if dels %2 == 1:
    if tryme == new:
        print("Deletion succeeded")
    else:
        print("Deletion failed")
else:
    if tryme == orig:
        print("Deletion succeeded")
    else:
        print("Deletion failed")
