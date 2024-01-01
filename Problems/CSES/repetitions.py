s = input()

prev = s[0]
count = 1
maxi = 1
for c in s[1:]:
    if prev == c:
        count += 1
        if count > maxi:
            maxi = count
    else:
        count = 1
        prev = c
print(maxi)


