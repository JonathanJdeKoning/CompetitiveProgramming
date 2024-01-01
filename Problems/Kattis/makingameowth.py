every, willing, youtime, meowtime = list(map(int, input().split()))


total = 0
page = 1
ew = 0
while True:
    
    if page%every == 0:
        total += meowtime
    else:
        total += youtime
        ew += 1

    page += 1
    if ew == willing:
        if page%every == 0:
            total += meowtime
        break
print(total)
