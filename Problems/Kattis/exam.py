correct = int(input())
you = input()
him = input()

matches = 0
diffs = 0

for i,c in enumerate(you):
    if c == him[i]:
        matches+=1
    else:
        diffs+=1
        

score = 0

while matches > 0:
    if correct == 0:
        break
    score += 1
    matches -= 1
    correct -= 1

score += diffs
score -= correct
print(score)
