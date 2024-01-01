ciphertext = input()
keyfix = input()
prefix = len(keyfix)
for idx, c in enumerate(ciphertext):
    cval = ord(c)-64
    kval = ord(keyfix[idx])-65

    goodval = (cval-kval)%26
    if goodval == 0:
        goodval = 26
    char = chr(goodval+64)
    keyfix+=char
print(keyfix[prefix:])