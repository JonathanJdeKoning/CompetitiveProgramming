parts, days = list(map(int, input().split()))

uniqs = []
good = True
for day in range(days):
    part = input()
    
    if part not in uniqs:
        uniqs.append(part)
        if len(uniqs) == parts:
            print(day+1)
            good = False
if good:
    print("paradox avoided")
    