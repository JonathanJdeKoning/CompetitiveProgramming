good= []
i = 1
while True:
    if i%3!=0 and str(i)[-1]!="3":
        good.append(i)
    i+=1
    if len(good) == 1002:
        break
for _ in range(int(input())):
    print(good[int(input())-1])
