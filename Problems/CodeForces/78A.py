a = len(list(filter(lambda x: x in "aeiou", list(input()))))
b = len(list(filter(lambda x: x in "aeiou", list(input()))))
c = len(list(filter(lambda x: x in "aeiou", list(input()))))

if a==5 and b==7 and c==5:
    print("YES")
else:
    print("NO")

