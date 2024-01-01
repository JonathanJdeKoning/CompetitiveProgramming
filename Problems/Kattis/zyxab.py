words = int(input())

mylist = []

for i in range(words):
    word = input()
    if len(word) < 5 or len(list(word)) != len(set(list(word))):
        continue
    mylist.append(word)

miny = 21
for word in mylist:
    if len(word) < miny:
        miny = len(word)

newarr = []

for word in mylist:
    if len(word) == miny:
        newarr.append(word)

try:
    print(sorted(newarr,reverse=True)[0])
except:
    print("neibb!")