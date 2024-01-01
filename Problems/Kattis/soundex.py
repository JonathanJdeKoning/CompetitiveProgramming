soundex= {
    "B":1,
    "F":1,
    "P":1,
    "V":1,
    "C":2,
    "G":2,
    "J":2,
    "K":2,
    "Q":2,
    "S":2,
    "X":2,
    "Z":2,
    "D":3,
    "T":3,
    "L":4,
    "M":5,
    "N":5,
    "R":6
}



while True:
    try:
        string = input()
        output = ""
        prev = None
        for c in string:
            if c in soundex:
                if prev != str(soundex[c]):
                    output += str(soundex[c])
                    prev = str(soundex[c])
            else:
                prev = None
        print(output)
    except EOFError:
        break
