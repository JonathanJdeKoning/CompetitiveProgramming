whoop = {
    "A":"",
    "B":"V",
    "C":"X",
    "D":"S",
    "E":"W",
    "F":"D",
    "G":"F",
    "H":"G",
    "I":"U",
    "J":"H",
    "K":"J",
    "L":"K",
    "M":"N",
    "N":"B",
    "O":"I",
    "P":"O",
    "Q":"",
    "R":"E",
    "S":"A",
    "T":"R",
    "U":"Y",
    "V":"C",
    "W":"Q",
    "X":"Z",
    "Y":"T",
    "Z":"",
    "1":"`",
    "2":"1",
    "3":"2",
    "4":"3",
    "5":"4",
    "6":"5",
    "7":"6",
    "8":"7",
    "9":"8",
    "0":"9",
    "-":"0",
    "=":"-",
    "[":"P",
    "]":"[",
    "\\":"]",
    ";":"L",
    "'":";",
    ",":"M",
    ".":",",
    "/":".",
    " ":" "
}
while True:
    try:
        new = ""
        for c in input():
            new+= whoop[c]
        print(new)
    except EOFError:
        break
