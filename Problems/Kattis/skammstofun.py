numwords = int(input())
caps = "ABCDEFGIHJKLMNOPQRSTUVWXYZ"
sentence = input()

out = ""

for word in sentence.split():
    if word[0] in caps:
        out += word[0]
print(out)