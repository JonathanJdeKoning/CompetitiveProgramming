w = int(input())
h = int(input())


string = ""
for i in range(h):
    string += input()
    
print(string.count(".")/len(string))