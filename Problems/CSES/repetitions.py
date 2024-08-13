s = input()
from itertools import groupby
print(max([len(x) for x in [list(v) for k, v in groupby(s)]]))


