d = {"............................xxxxxxx.......":"1",
    "xxxx..xx..x..xx..x..xx..x..xx..xxxx.......":"2",
    "x..x..xx..x..xx..x..xx..x..xxxxxxxx.......":"3",
    "...xxxx...x......x......x...xxxxxxx.......":"4",
    "x..xxxxx..x..xx..x..xx..x..xxxxx..x.......":"5",
    "xxxxxxxx..x..xx..x..xx..x..xxxxx..x.......":"6",
    "......x......x......x......xxxxxxxx.......":"7",
    "xxxxxxxx..x..xx..x..xx..x..xxxxxxxx.......":"8",
    "x..xxxxx..x..xx..x..xx..x..xxxxxxxx.......":"9",
    "xxxxxxxx.....xx.....xx.....xxxxxxxx.......":"0",
    "...x......x....xxxxx....x......x..........":"+"}
e = {v:k for k, v in d.items()}

mat = []
for _ in range(7):
    mat.append(list(input()))

mat = list(zip(*mat[::-1]))
s=""
for row in mat:
    s+= "".join(row)
s += "......."

for key, val in d.items():
    s = s.replace(key, val)
res = eval(s)

new = ""

for c in str(res):
    new+=e[c]
new = new[:-7]

newmat = []
for i in range(0,len(new),7):
    newmat.append(list(new[i:i+7]))
newmat = list(zip(*newmat))[::-1]

for row in newmat:
    print("".join(row))


