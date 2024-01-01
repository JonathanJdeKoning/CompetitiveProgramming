symbdict = {
    "a":"@",
    "b":"8",
    "c":"(",
    "d":"|)",
    "e":"3",
    "f":"#",
    "g":"6",
    "h":"[-]",
    "i":"|",
    "j":"_|",
    "k":"|<",
    "l":"1",
    "m":"[]\/[]",
    "n":"[]\[]",
    "o":"0",
    "p":"|D",
    "q":"(,)",
    "r":"|Z",
    "s":"$",
    "t":"']['",
    "u":"|_|",
    "v":"\/",
    "w":"\/\/",
    "x":"}{",
    "y":"`/",
    "z":"2"}

string = input().lower()
output = ""
for c in string:
    if c in symbdict:
        output += symbdict[c]
    else:
        output += c
print(output)