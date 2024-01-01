numcomps, numreqs = list(map(int, input().split()))

companies = {}

compin = input().split()

for idx, comp in enumerate(compin):
    companies[idx+1] = int(comp)

for req in range(numreqs):
    reqstr = list(map(int, input().split()))

    query = reqstr[0]
    a = reqstr[1]
    b = reqstr[2]

    if query == 1:
        companies[a] = b
    else:
        print(abs(companies[a]-companies[b]))


