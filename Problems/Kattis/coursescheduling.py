reqs = int(input())
mydict = {}
for req in range(reqs):
    first, last, course = input().split()
    name = first + " " + last
    if course not in mydict:
        mydict[course] = [name]
    else:
        if name in mydict[course]:
            continue
        else:
            mydict[course].append(name)
for course in sorted(mydict):
    print(f"{course} {len(mydict[course])}")
