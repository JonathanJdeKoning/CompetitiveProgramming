s = []
for i in range(1, 500000):
    s.append(str(i))

s = "".join(s)
print(s[:200])
print(
    int(s[0])
    * int(s[9])
    * int(s[99])
    * int(s[999])
    * int(s[9999])
    * int(s[99999])
    * (int(s[999999]))
)
