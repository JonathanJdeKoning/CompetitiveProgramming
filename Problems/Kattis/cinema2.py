seats, groups = list(map(int, input().split()))

people = list(map(int, input().split()))

count = 0
for person in people:
   if seats - person < 0:
       count += 1
       seats = -1
   else:
       seats -= person
    
print(count) 