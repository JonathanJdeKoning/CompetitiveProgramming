n,m = map(int, input().split())
pieces = set()
for _ in range(n):
    for piece in list(map(int, input().split()))[1:]:
        pieces.add(piece)
if sorted(list(pieces)) == list(range(1,m+1)):
    print("Jebb")
else:
    print("Neibb")
