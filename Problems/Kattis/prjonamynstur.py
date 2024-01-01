string = ""
n, m = list(map(int, input().split()))

for i in range(n):
    string+= input()
    
count = 0

count += string.count(".")*20
count += string.count("O")*10
count += string.count("\\")*25
count += string.count("/")*25
count += string.count("A")*35
count += string.count("^")*5
count += string.count("v")*22

print(count)