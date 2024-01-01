questions = int(input())

test = input()
adrian = "ABC"*34
bruno = "BABC"*25
goran = "CCAABB"*17

goodas = 0
goodbs = 0
goodgs = 0

for i in range(questions):
    if test[i] ==adrian[i]:
        goodas +=1
    if test[i] == bruno[i]:
        goodbs += 1
    if test[i] == goran[i]:
        goodgs += 1

maxi = max([goodas, goodbs, goodgs])
print(maxi)

if goodas == maxi:
    print("Adrian")
if goodbs == maxi:
    print("Bruno")
if goodgs == maxi:
    print("Goran")