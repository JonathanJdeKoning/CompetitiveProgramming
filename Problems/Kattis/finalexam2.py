qs = int(input())

test = []
total = 0
for q in range(qs):
    test.append(input())

hanh = test[1:]
for q in range(qs):
    try:
        if test[q] == hanh[q]:
            total += 1
    except:
        pass
print(total)