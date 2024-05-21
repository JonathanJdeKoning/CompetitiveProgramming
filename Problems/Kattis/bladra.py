numProblems, numSolved = map(int, input().split())
d = {}
for i in range(1,numProblems+1):
    d[i] = 0
for _ in range(numSolved):
    team, problem = map(int, input().split())
    d[problem] += 1
print(min(d.values()))
