memes = int(input())
mx = 0
best = []
for _ in range(memes):
    meme, contro,cool = input().split()
    contro = int(contro)
    cool = int(cool)
    
    fresh = contro + cool
    if fresh > mx:
        mx = fresh
        best = [meme]
    elif fresh == mx:
        best.append(meme)
        
print(sorted(best)[0])
    
