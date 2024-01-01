votes = {}

while True:
    vote = input()
    if vote == "***": break


    if vote not in votes:
        votes[vote] = 1
    else:
        votes[vote] += 1
    

   
maxvotes = max(votes.values())
 
winner = []


for vote, count in votes.items():
    if count == maxvotes:
        winner.append(vote)

if len(winner) > 1:
        print("Runoff!")
else: print(winner[0])