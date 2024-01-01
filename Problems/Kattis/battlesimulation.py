import re
mystr = input()
mystr = re.sub('RLB|RBL|BLR|BRL|LRB|LBR', 'C', mystr)
mystr = mystr.translate(mystr.maketrans('LBR', 'HKS'))
print(mystr)
