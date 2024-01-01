nums = int(input())

good = list(range(1,nums+1))

alex = input().split()

test = []
count = 1
for thing in alex:
    if thing == "mumble":
        test.append(count)
    else:
        test.append(int(thing))
    count += 1


if test == good:
    print("makes sense")
else:
    print("something is fishy")