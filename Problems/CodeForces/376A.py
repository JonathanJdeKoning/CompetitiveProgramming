s = input()

left = 0
right = 0

pivot = s.index("^")
l = True
for i, c in enumerate(s):
    if c in "=": continue
    if c== "^":
        l = False
        continue 
    if l:
        left += int(c)*(abs(pivot-i))
    else:
        right += int(c)*(abs(pivot-i))

if left == right:
    print("balance")
elif left > right:
    print("left")
else:
    print("right")
    
    
