def c2d(c):
    return ord(c) - 96

word = input()

for c in word:
    print(bin(c2d(c))[2:],end = "")
