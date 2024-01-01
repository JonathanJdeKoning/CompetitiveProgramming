num = int(input())

print(int(str(bin(num).replace("0b", ""))[::-1],2))