blocks = int(input())

totalblocks = 0
layercount = 0
for i in range(1,1000000,2):
    layercount+=1
    layer = i*i
    
    totalblocks += layer
    
    if totalblocks > blocks:
        totalblocks -= layer
        print(layercount-1)
        break
    
    