string = input()

third = len(string) // 3

a = string[0:third]
b = string[third: third*2]
c = string[third*2:]

mylist = [a,b,c]

for word in mylist:
    if mylist.count(word) >= 2:
        print(word)
        break