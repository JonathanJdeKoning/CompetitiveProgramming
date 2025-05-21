from itertools import* 
input()
print(len([x for x in list(groupby(zip(input(),input()),key=lambda x:x[0]==x[1]))if not x[0]]))