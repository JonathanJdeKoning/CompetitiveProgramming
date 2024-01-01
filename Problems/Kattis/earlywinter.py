years, snow = list(map(int, input().split()))
good = False
snowdata = list(map(int, input().split()))
for idx, year in enumerate(snowdata):
    if year <= snow:
        snow = idx
        good = True
        break

if good == True:
    print(f"It hadn't snowed this early in {snow} years!")
else:
    print("It had never snowed this early!")

