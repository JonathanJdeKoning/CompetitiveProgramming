string = input()
cards = [string[i:i+3] for i in range(0, len(string), 3)]
bad = False
if len(cards) != len(set(cards)):
    print("GRESKA")
    bad = True

p = 13
k = 13
h = 13
t = 13
if not bad:
    for card in cards:
        suit = card[0]
        
        if suit == "P":
            p -= 1
        elif suit == "K":
            k -=1
        elif suit == "H":
            h -=1
        elif suit == "T":
            t -= 1
            
    print(" ".join([str(x) for x in [p,k,h,t]]))