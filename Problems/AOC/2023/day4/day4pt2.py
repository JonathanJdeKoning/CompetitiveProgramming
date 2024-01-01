sum = 0
carddict = {}
copies = {}
with open("input.txt", "r") as file:
    for line in [x.strip() for x in file.readlines()]:
        
        data = line.replace(":", "|").split("|")
        cardid = data[0].split()[1]
        winners = data[1].split()
        nums = data[2].split()
        
        total = len([x for x in nums if x in winners])
        carddict[cardid] = total
        copies[cardid] = 1

print(carddict)
for key, val in carddict.items():
    checkthis = [str(x) for x in list(range(int(key)+1,int(key)+val+1))]
    
    for check in checkthis:
        copies[check] += copies[key]  
sum = 0
for x in copies.values():
    sum += x
print(sum)
