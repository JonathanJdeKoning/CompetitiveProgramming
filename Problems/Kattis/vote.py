tests = int(input())

for test in range(tests):
 
    votelist = []
    votes = int(input())
    for i in range(votes):
        vote = int(input())
        votelist.append(vote)

    top = max(votelist)
    idx = votelist.index(top)+1

    votelist = sorted(votelist, reverse=True)

    if votelist[0] == votelist[1]:
        print("no winner")
        continue

    therest = sum(votelist) - top

    if top > therest:
        print(f"majority winner {idx}")
    else:
        print(f"minority winner {idx}")
