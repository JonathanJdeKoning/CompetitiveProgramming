cards = input().split()
cards = [x[0] for x in cards]
m = max(map(cards.count, cards))
print(m)
