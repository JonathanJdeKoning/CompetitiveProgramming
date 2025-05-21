s = "Á,a á,a Ð,d ð,d É,e é,e Í,i í,i Ó,o ó,o Ú,u ú,u Ý,y ý,y Þ,th þ,th Æ,ae æ,ae Ö,o ö,o"
pairs = s.split()
mp = {k:v for pair in pairs for k,v in [pair.split(",")]}

new = []
good = "qwertyuiopasdfghjklzxcvbnm"
s = input()
for c in s:
    if c in mp:
        new.append(mp[c])
        continue
    if c.lower() not in good: continue
    new.append(c.lower())
print("".join(new) + ".is")