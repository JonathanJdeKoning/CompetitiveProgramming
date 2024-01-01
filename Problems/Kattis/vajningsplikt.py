arrive, want, come = input().split()

leftdict = {
    "South": "West",
    "West": "North",
    "North": "East",
    "East": "South"
}
rightdict = {
    "South": "East",
    "East": "North",
    "North" : "West",
    "West": "South"
}
straightdict = {
    "North": "South",
    "South": "North",
    "West": "East",
    "East": "West"
}

if want == straightdict[arrive] and come == rightdict[arrive]:
    print("Yes")
elif want == leftdict[arrive] and (come == rightdict[arrive] or come ==straightdict[arrive]):
    print("Yes")
else:
    print("No")