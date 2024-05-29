n = int(input())
years = n//365
n %= 365
months = n//30
n%=30
print(f"{years} years")
print(f"{months} months")
print(f"{n} days")
