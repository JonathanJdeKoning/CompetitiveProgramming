s = "".join([x.lower() for x in input() if x.isalpha()])
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        t = s[i:j]
        if len(t) < 2: continue
        if t == t[::-1]: exit(print("Palindrome"))

print("Anti-palindrome") 