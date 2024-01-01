tests = int(input())

for test in range(tests):
    str1 = input()
    str2 = input()
    output = ""
    
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            output += "."
        else:
            output += "*"
    print(str1)
    print(str2)
    print(output)
    print()