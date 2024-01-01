players = int(input())

mylist = []

for i in range(players):
    mylist.append(input())


asc = sorted(mylist)
desc = sorted(mylist, reverse=True)
if mylist == asc:
    print("INCREASING")
elif mylist == desc:
    print("DECREASING")
else:
    print("NEITHER")
