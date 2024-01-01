minutes, songs = list(map(int, input().split()))

seconds = minutes*60

songlist = sorted(list(map(int, input().split())))

totalseconds = 0
for song in songlist:
    if seconds - song >= 0:
        totalseconds += song
        seconds -= song
print(totalseconds)