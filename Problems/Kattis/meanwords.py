numwords = int(input())
import math
words = []
for i in range(numwords):
    words.append(input())

words = sorted(words, key=len, reverse=True)
base = len(words[0])

output = ""
for i in range(base):
    total = 0
    wordtotal = 0
    for word in words:
        try:
            total += ord(word[i])
            wordtotal += 1
        except:
            pass
    output+=chr(int(math.floor(total/wordtotal)))
print(output)

