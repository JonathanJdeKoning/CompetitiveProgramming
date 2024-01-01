words = input().split()
uniq = set(words)

if len(words) != len(uniq):
    print("no")
else: print("yes")