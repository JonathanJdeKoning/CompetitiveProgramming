m = list(map(int, input().split()))
w = list(map(int, input().split()))
succ, unsucc = map(int, input().split())


score = 0

for i in range(5):
    x = (i+1)*500
    q = max(0.3*x,(1-m[i]/250)*x - 50*w[i])
    score += q

score += succ*100
score -= unsucc*50

print(int(score))

"""
3 6 13 38 60
6 10 10 3 8
9 9
"""
