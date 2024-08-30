startH, startM = map(int, input().split(":"))
endH, endM = map(int, input().split(":"))


from datetime import datetime
startSmall = True

if endH < startH:
    startSmall = False
elif endH==startH:
    if startM > endM:
        startSmall = False

if startSmall:
    then = datetime(2024, 7, 12, startH, startM, 0)
    now = datetime(2024, 7, 12, endH, endM, 0)
    duration = now - then
    print(int(duration.total_seconds()//60))
else:
    then = datetime(2024, 7, 12, startH, startM, 0)
    now = datetime(2024, 7, 13, endH, endM, 0)
    duration = now - then
    print(int(duration.total_seconds()//60))

