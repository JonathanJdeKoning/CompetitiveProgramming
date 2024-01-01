climb, fall, height = list(map(int, input().split()))

count = 0 
progress = 0
while(progress <= height):
    progress += climb
    count += 1
    
    if progress >= height: break

    progress -= fall
print(count)