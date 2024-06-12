import heapq
input()
kor = list(map(lambda x:(int(x),1), input().split()))
wes = (list(map(lambda x:(int(x), 2), input().split())))
chi = (list(map(lambda x:(int(x), 3), input().split())))
kor.sort()
wes.sort()
chi.sort()

for _ in range(int(input())):
    k,w,c,x = map(int, input().split())

    h = []
    for i in range(k):
        heapq.heappush(h, kor[i])
    for i in range(w):
        heapq.heappush(h, wes[i])
    for i in range(c):
        heapq.heappush(h, chi[i])

    print(heapq.nsmallest(x, h)[-1])
