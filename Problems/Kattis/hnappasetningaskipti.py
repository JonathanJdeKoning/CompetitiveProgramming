q2d = {"~":"~",
"1":"1",
"2":"2",
"3":"3",
"4":"4",
"5":"5",
"6":"6",
"7":"7",
"8":"8",
"9":"9",
"0":"0",
"-":"[",
"=":"]",
"q":"'",
"w":",",
"e":".",
"r":"p",
"t":"y",
"y":"f",
"u":"g",
"i":"c",
"o":"r",
"p":"l",
"[":"/",
"]":"=",
"a":"a",
"s":"o",
"d":"e",
"f":"u",
"g":"i",
"h":"d",
"j":"h",
"k":"t",
"l":"n",
";":"s",
"'":"-",
"z":";",
"x":"q",
"c":"j",
"v":"k",
"b":"x",
"n":"b",
"m":"m",
",":"w",
".":"v",
"/":"z",
" ":" "}

d2b = {"~":"0",
"1":"2",
"2":"4",
"3":"8",
"4":"6",
"5":"1",
"6":"3",
"7":"5",
"8":"7",
"9":"9",
"0":"=",
"[":"-",
"]":"/",
"'":"b",
",":"j",
".":"a",
"p":"r",
"y":"k",
"f":"i",
"g":"g",
"c":"u",
"r":"s",
"l":"t",
"/":".",
"=":",",
"a":"l",
"o":"o",
"e":"e",
"u":"m",
"i":"p",
"d":"d",
"h":"c",
"t":"n",
"n":"v",
"s":"q",
"-":";",
";":"[",
"q":"]",
"j":"y",
"k":"z",
"x":"h",
"b":"w",
"m":"f",
"w":"x",
"v":"'",
"z":"~",
" ":" "}

q2q = {k:k for k,v in q2d.items()}
d2d = {v:v for k,v in q2d.items()}
b2b = {v:v for k,v in d2b.items()}
d2q = {v:k for k,v in q2d.items()}
b2d = {v:k for k,v in d2b.items()}
q2b = {k:d2b[v] for k,v in q2d.items()}
b2q = {v:k for k,v in q2b.items()}

data = input().split()
a, b = data[0], data[2]
out = []

for c in input():
    if a == b:
        out.append(c)
    elif a == "qwerty" and b == "dvorak":
        out.append(q2d[c])
    elif a == "qwerty" and b == "bjarki":
        out.append(q2b[c])
    elif a == "dvorak" and b == "qwerty":
        out.append(d2q[c])
    elif a == "dvorak" and b == "bjarki":
        out.append(d2b[c])
    elif a == "bjarki" and b == "dvorak":
        out.append(b2d[c])
    elif a == "bjarki" and b == "qwerty":
        out.append(b2q[c])

print("".join(out))


