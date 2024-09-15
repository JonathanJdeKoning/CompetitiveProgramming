rule, length, n = map(int, input().split())

curr = input()
patterns = ["111", "110", "101", "100", "011", "010", "001", "000"]
rule = bin(rule)[2:]
d = {}
for i, c in enumerate(rule.zfill(8)):
    d[patterns[i]] = c 

#print(d)
for q in range(1,n+1):
    row = []
    curr = "0"+curr+"0"
    for i in range(len(curr)):
        if i == 0:
            chk = "0" + curr[:2]
        elif i == len(curr)-1:
            chk = curr[-2:] +"0"
        else:
            chk = curr[i-1] + curr[i] + curr[i+1]
        #print(f"{i=}, {chk=}")
        row.append(d[chk])
    row = "".join(row)
    print(row[q:-q].replace("0", "⬛").replace("1", "⬜"))
    curr = row


