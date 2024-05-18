half = int(input())

s = input()

one = sorted([int(x) for x in list(s[:half])])
two = sorted([int(x) for x in list(s[half:])])

three = [a-b for a,b in zip(one,two)]
four = [b-a for a,b in zip(one,two)]

if len([x for x in three if x > 0])==len(three) or len([x for x in four if x > 0])==len(four):
    print("YES")
else:
    print("NO")
