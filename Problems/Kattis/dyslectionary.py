while True:
    try:
        words = []
        mx = 0
        while True:
            word = input()
            if word == "":
                break
            words.append(word)
            mx = max(mx, len(word))

        for i, word in enumerate(words):
            words[i] = word.rjust(mx)

        print("\n".join(sorted(words, key=lambda x:x[::-1])))
        print()
    except EOFError: break

for i, word in enumerate(words):
    words[i] = word.rjust(mx)


print("\n".join(sorted(words, key=lambda x:x[::-1])))
