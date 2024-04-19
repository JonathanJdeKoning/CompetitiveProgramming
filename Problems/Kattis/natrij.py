from datetime import datetime
s1 = input()
s2 = input()
FMT = '%H:%M:%S'
out = str(datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT))
if "," in out:
    out = out[out.index(",")+2:]

if len(out) == 7:
    out = "0"+out

if out == "00:00:00":
    out = "24:00:00"
print(out)
