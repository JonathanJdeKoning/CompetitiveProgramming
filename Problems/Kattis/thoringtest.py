good = set()
for _ in range(int(input())):
    good.add(input().lower())

s = input().lower().split()
for word in s:
    if word not in good:
        exit(print("Thore has left the chat"))
print("Hi, how do I look today?")

