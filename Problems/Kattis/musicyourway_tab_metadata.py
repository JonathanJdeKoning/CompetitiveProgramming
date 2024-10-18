attr = input().split()
mp = {attr[i]: i for i in range(len(attr))}
N = int(input())
songs = []
for _ in range(N):
    songs.append(input().split())

K = int(input())
for _ in range(K):
    s = input()
    songs = sorted(songs, key=lambda x: x[mp[s]])
    print(" ".join(attr))
    for song in songs:
        print(" ".join(song))
    print()