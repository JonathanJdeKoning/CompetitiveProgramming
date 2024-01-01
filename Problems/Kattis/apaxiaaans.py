word = input()
new = ""
oldletter = ""
for letter in word:
    if letter != oldletter:
        new += letter
    oldletter = letter

print(new)