from collections import Counter
s = {"A":1, "K":2, "Q":3,"J":4, "T":5, "9":6, "8":7, "7":8, "6":9, "5":10, "4":11, "3":12, "2":13}

bids, hands, sum = {}, [], 0
with open("input.txt", "r") as file:
    lines = [x.strip() for x in file.readlines()]
    for line in lines:
        hand, bid = line.split()
        bids[hand] = int(bid)
        hands.append(hand)

mult = len(hands)
fives = sorted([hand for hand in hands if 5 in Counter(hand).values()], key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))
fours = sorted([hand for hand in hands if 4 in Counter(hand).values()], key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))
fulls = sorted([hand for hand in hands if 3 in Counter(hand).values() and 2 in Counter(hand).values()], key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))
threes = sorted([hand for hand in hands if 3 in Counter(hand).values() and 1 in Counter(hand).values()], key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))
pairs = sorted([hand for hand in hands if list(Counter(hand).values()).count(2) == 2], key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))
twos = sorted([hand for hand in hands if list(Counter(hand).values()).count(2) == 1 and list(Counter(hand).values()).count(1) == 3], key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))
ones = sorted([hand for hand in hands if len(Counter(hand).values()) == 5], key=lambda x:(s[x[0]], s[x[1]], s[x[2]], s[x[3]],s[x[4]]))

sortedhands = fives+fours+fulls+threes+pairs+twos+ones

for hand in sortedhands:
    sum+=bids[hand]*mult
    mult-=1
print(sum)
