a = input()
b = input()
c = input()

n = str(int(a)*int(b)*int(c))

out = []
for i in range(10):
    print(n.count(str(i)))

