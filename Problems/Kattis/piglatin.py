while True:
    try:
        words = input().split()
        out = []
        for word in words:
            new = ""
            if word[0] in "aeiouy":
                new = word + "yay"
            else:
                consos = ""
                for idx, c in enumerate(word):
                    if c not in "aeiouy":
                        consos+=c
                    else:
                        new = word[idx:] + "".join(consos) + "ay"
                        break
            out.append(new)
        print(" ".join(out))
    except EOFError:
        break
