days = int(input())

you = list(map(int,input().split()))
them = list(map(int,input().split()))
that = list(map(int,input().split()))

output = ""
for i in range(days):
    output += str(sorted([you[i], them[i], that[i]])[1]) + " "

print(output[:-1])
