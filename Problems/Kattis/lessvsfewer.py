nouns, phrases = list(map(int, input().split()))

noundict = {}

proper = {
    "number of" :"c",
    "amount of": "m",
    "most": "e",
    "fewest": "c",
    "least": "m",
    "more": "e",
    "fewer": "c",
    "less": "m",
    "many": "c",
    "much": "m",
    "few": "c",
    "little":"m"
}

for i in range(nouns):
    noun, ntype = input().split()
    noundict[noun] = ntype

for i in range(phrases):
    phrase = input().split()
    noun = phrase[-1]
    pre = " ".join(phrase[0:-1])
    
    if proper[pre] == noundict[noun] or proper[pre] == "e":
        print("Correct!")
    else:
        print("Not on my watch!")


