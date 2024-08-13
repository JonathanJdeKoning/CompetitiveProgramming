s, e = map(int, input().split())
def numberofways(s, e):
    if s == e: return 1
    if s > e: return 0
    return numberofways(s+1, e) + numberofways(s+2, e) + numberofways(s+3, e)

print(numberofways(s,e))
