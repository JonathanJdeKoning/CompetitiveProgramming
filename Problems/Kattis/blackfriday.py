nums = int(input())
things = list(map(int, input().split()))
new = [x for x in things if things.count(x) == 1]
if len(new)== 0 :
    print("none")
else:
    print(things.index(max(new))+1)
