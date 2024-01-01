hotels = int(input())

hotellist = list(map(int, input().split()))

probdict = {
    "2" :2.778,
    "3" :5.556,
    "4" :8.333,
    "5" :11.111,
    "6" :13.889,
    "7" :16.667,
    "8" :13.889,
    "9" :11.111,
    "10" :8.333,
    "11" :5.556,
    "12" :2.778,
}
summy = 0
for item in hotellist:
    summy += probdict[str(item)]

print(summy/100)