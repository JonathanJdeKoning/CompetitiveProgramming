numcards = int(input())

cards = sorted(list(map(int, input().split())))

curr = cards[0]
total = curr
for card in cards[1:]:
    if card == curr+1:
        curr += 1
        continue
    else:
        total += card
        curr = card

print(total)