import re
string = input()
a = [m.start() for m in re.finditer('\:\)',string)]
b = [m.start() for m in re.finditer('\;\)',string)]
c = [m.start() for m in re.finditer('\:\-\)',string)]
d = [m.start() for m in re.finditer('\;\-\)',string)]
myarr = sorted(a + b + c + d)

for num in myarr:
    print(num)
