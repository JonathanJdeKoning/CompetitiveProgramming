secret = input()
guess = input()
from collections import Counter, defaultdict

sFQ = Counter(secret)
gFQ = Counter(guess)
right = defaultdict(int)
out = ["-"]*5
for i in range(5):
    if secret[i] == guess[i]:
        out[i] = "G"
        right[secret[i]] += 1


for c in sFQ:
    x = sFQ[c]
    y = gFQ[c]

    yRem = y - right[c]
    xRem = x - right[c]

    for i in range(5):
        if guess[i] == c and xRem and out[i] != "G":
            xRem -= 1
            out[i] = "Y"

print("".join(out))
