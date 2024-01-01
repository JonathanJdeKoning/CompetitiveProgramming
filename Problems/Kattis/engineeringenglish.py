seen = []
while True:
    try:
        out = ""
        line = input().split()
        for word in line:
            word = word.lower()
            if word not in seen:
                out += word + " "
                seen.append(word)
            else:
                out += ". "
        print(out[:-1])

    except EOFError:
        break
