n,k = map(int, input().split())
words = input().split()

currline = []
charsLeft = k
for word in words:
    if charsLeft >= len(word):
        currline.append(word)
        charsLeft -= len(word)
    else:
        print(" ".join(currline))
        currline = [word]
        charsLeft = k-len(word)

if currline:
    print(" ".join(currline))


