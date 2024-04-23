from collections import defaultdict


def solve():
    numCandidates = int(input())

    parties = {}
    candidates = set()

    for _ in range(numCandidates):
        candidate = input()
        candidates.add(candidate)
        party = input()
        
        if party == "independent":
            parties[candidate] = " "+candidate
        else:
            parties[candidate] = party



    votes = defaultdict(int)

    numVotes = int(input())
    for _ in range(numVotes):
        vote = input()
        if vote not in candidates: continue
        party = parties[vote]
        votes[party] += 1

    voteTotals = votes.values()
    try:
        mx = max(voteTotals)
    except: return "tie"
    winners = []
    for vote, total in votes.items():
        if total == mx:
            winners.append(vote)
    if len(winners) != 1:
        return "tie"

    if winners[0][0] == " ":
        return 'independent'
    return winners[0]

print(solve())



