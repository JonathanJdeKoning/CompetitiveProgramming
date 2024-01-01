def ordinal(n):
    if n == 0:
        return "{}"
    else:
        mylist = []

        for i in range(n):
            mylist.append(ordinal(i))
        return "{" +",".join(mylist) + "}"

print(ordinal(int(input())))


#print(ordinal(0))
#print(ordinal(1))
#print(ordinal(2))
#print(ordinal(3))
#print(ordinal(4))
#print(ordinal(5))
#print(ordinal(6))
#print(ordinal(7))
#print(ordinal(8))
