judges, rated = list(map(int, input().split()))

badArr = []
goodArr= []
for i in range(rated):
    rating = int(input())
    badArr.append(rating)
    goodArr.append(rating)
    
for i in range(judges - rated):
    badArr.append(-3)
    goodArr.append(3)
print(f"{sum(badArr)/len(badArr)} {sum(goodArr)/len(goodArr)}")