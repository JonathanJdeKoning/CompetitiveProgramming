word = input()

guess = input()

bads = 0
for letter in guess:
    if bads == 10:
        print("LOSE")
    if letter in word:
        
        word = word.replace(letter, "")
        if word == "":
            print("WIN")
            break
        else:
            continue
    else:
        bads += 1
        if bads == 10:
            print("LOSE")
            break