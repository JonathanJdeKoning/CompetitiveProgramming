d1, m1 ,y1, n = list(map(int, input().replace(","," ").split()))
d2,m2,y2 = list(map(int, input().replace(","," ").split()))

dayslater = 0
dayslater += 360*(y2-y1)
dayslater += 30*(m2-m1)
dayslater += (d2-d1)

ans = ((dayslater+n)%7)
if ans == 0: ans = 7
print(ans)