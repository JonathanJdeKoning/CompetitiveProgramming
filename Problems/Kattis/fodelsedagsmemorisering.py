friends = int(input())

bdaydict = {}
for friendnum in range(friends):
    friend, like, bday = list(input().split())
    like = int(like)
    if bday not in bdaydict:
        bdaydict[bday] = [friend, like]
    else:
        if like > bdaydict[bday][1]:
            bdaydict[bday] = [friend,like]

friendslist = []
for bday, namelike in bdaydict.items():
    friendslist.append(namelike[0])
print(len(friendslist))
print("\n".join(sorted(friendslist)))

    