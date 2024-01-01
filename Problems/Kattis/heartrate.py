tests = int(input())


for i in range(tests):
    b, p = list(map(float, input().split()))

    bpm = (60*b)/p
    variance = 60/ p 


    mini = bpm - variance
    maxi = bpm + variance
    print(" ".join([str(mini), str(bpm), str(maxi)]))