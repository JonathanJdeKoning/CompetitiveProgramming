letters = {"clank": "a",
            "bong":"b",
            "click":"c",
            "tap": "d",
            "poing": "e",
            "clonk": "f",
            "clack": "g",
            "ping": "h",
            "tip": "i",
            "cloing": "j",
            "tic": "k",
            "cling": "l",
            "bing": "m",
            "pong": "n",
            "clang" : "o",
            "pang":"p",
            "clong":"q",
            "tac":"r",
            "boing":"s",
            "boink":"t",
            "cloink":"u",
            "rattle":"v",
            "clock":"w",
            "toc":"x",
            "clink":"y",
            "tuc":"z",
            "whack": " "
            }
out = []
lower = True
for i in range(int(input())):
    word = input()
    if word == "pop":
        if len(out) > 0:
            out.pop()
        continue
    if word == "bump"or word == "dink" or word == "thumb": 
        lower = not lower
        continue
    if lower:
        out.append(letters[word])
    else:
        out.append(letters[word].upper())
print("".join(out))
    
