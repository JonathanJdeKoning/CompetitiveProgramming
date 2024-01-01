words = []

for _ in range(int(input())):
    words.append(input())
    
for word in words[::2]:
    print(word)