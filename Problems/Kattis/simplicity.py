from collections import Counter
s = input()
data = list(Counter(s).values())
tot = 0
while len(data)>2:
    mini = min(data)
    tot += mini
    data.remove(mini)
print(tot)

