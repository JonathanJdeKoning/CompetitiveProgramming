from itertools import groupby
numwords = int(input())
menu = input().split()
vowels = "aeiou"
mylist = []
for word in menu:
    new = ""
    reps = [list(g) for k, g in groupby(word)]
    for rep in reps:
        new+= rep[0]
    newnew = ""
    
    if len(new) > 1:
        newnew+= new[0]
        for c in new[1:-1]:
            if c not in vowels:
                newnew+=c
        newnew+= new[-1]
    else:
        newnew = new
    mylist.append(newnew)
print(" ".join(mylist))
