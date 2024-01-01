hours, minutes = list(map(int, input().split()))

if minutes >= 45:
    print(f"{hours} {minutes-45}")
else:
    if hours == 0:
        hours = 24
    print(f"{hours-1} {60+(minutes-45)}")