month, day, year = list(map(int,input().split("/")))

if month > 12:
    print("EU")
if day > 12:
    print("US")
if month <= 12 and day <= 12:
    print("either")