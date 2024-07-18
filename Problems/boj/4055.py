day = 0
while True:
    day += 1
    n = int(input())
    if n==0: break
    starts = set()
    parties = []
    for _ in range(n):
        start, end = map(int, input().split())
        parties.append((start, end))
    parties.sort(key=lambda x:x[1]-x[0])
    for start, end in parties:
        while start != end:
            if start not in starts:
                starts.add(start)
                break
            start += 0.5
    
    print(f"On day {day} Emma can attend as many as {len(starts)} parties.")
