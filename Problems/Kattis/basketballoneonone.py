string = input()

a = 0
b = 0

a+= 2*string.count("A2")
a+= string.count("A1")
b+= 2*string.count("B2")
b+= string.count("B1")

print("A") if a > b else print("B")