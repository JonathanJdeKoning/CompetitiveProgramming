forbidden = input()

sentence = input().split()
output = ""
    
for word in sentence:
    good = True

    for letter in forbidden:
        if letter in word:
            output += ("*"*len(word))
            good = False
            break
    if good:
        output += word
    output += " "
print(output[:-1])