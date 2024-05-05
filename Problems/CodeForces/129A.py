numbags = int(input())
cookies = list(map(int, input().split()))
print(len([x for x in cookies if (sum(cookies) - x)%2==0]))
