javs = int(input())

length = 0
for i in range(javs):
    length+= int(input())
length -= (javs-1)
print(length)