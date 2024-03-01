numpassengers, numplanes = map(int, input().split())
emptyseats = list(map(int, input().split()))
passers = numpassengers
emp = emptyseats[:]
mx = 0

while numpassengers > 0:
    numpassengers -= 1
    mxseat = max(emptyseats)
    mx += mxseat
    emptyseats[emptyseats.index(mxseat)] -= 1
mn = 0

while passers > 0:
    passers -= 1
    mnseat = min([x for x in emp if x >0])
    mn += mnseat
    emp[emp.index(mnseat)] -= 1
print(mx, mn)
