hands, dom = input().split()
hands = int(hands)
points = 0

carddict = {
    "A": 11,
    "K" : 4,
    "Q" : 3,
    "J" : 20,
    "T": 10,
    "9": 14,
    "8": 0,
    "7": 0}

for cardnum in range(4*hands):
    card = input()
    cardsuit = card[1]
    cardval = card[0]
    
    if cardsuit == dom:
        points += carddict[cardval]
    else:
        if cardval == "J":
            points += 2
        elif cardval == "9":
            points += 0
        else:
            points += carddict[cardval]
print(points)
    
    