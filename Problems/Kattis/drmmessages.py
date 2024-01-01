string = input()

length = len(string)
a = string[:length//2]
b = string[length//2:]

def cnum(c):
    return (ord(c)-65)
asum = sum([cnum(c) for c in a])
bsum = sum([cnum(c) for c in b])

a = [chr(65+((cnum(c)+asum)%26)) for c in a]
b = [chr(65+((cnum(c)+bsum)%26)) for c in b]


new = ""
for i,c in enumerate(a):
    new+= chr(65+((cnum(c)+cnum(b[i]))%26))
print(new)
