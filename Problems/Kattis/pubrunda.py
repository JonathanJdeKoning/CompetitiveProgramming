num = int(input())
mini = 0
minname=""
for _ in range(num):
    data = input().split()
    if int(data[1])*int(data[2])+int(data[2]) > mini: 
        mini = int(data[1])*int(data[2])+int(data[2])
        minname = data[0]
print(f"{minname} {mini}")
