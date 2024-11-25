def shift(s):
    return "".join([chr((((ord(x)-97)+1)%26)+97) for x in s])
s = input()
for i in range(27):
    if s == "branksomeh": exit(print("BHA"))
    if s == "stjohnsbur": exit(print("SJA"))
    if s == "northlondo": exit(print("NLCS"))
    if s == "koreainter": exit(print("KIS"))
    s = shift(s)