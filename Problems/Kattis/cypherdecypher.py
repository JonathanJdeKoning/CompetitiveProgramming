key = input()

numwords = int(input())

for i in range(numwords):
    word = input()
    out = ""
    for i, c in enumerate(word):
        out+= chr((((ord(c)-65)*int(key[i])) % 26) + 65)
    print(out)
        