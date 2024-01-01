import re
import math
string = input()
need = "0"
matches = re.findall(need + "+", string)
try:
    res = len(max(matches, key=len))
except:
    res = 0
print(int(math.ceil(res/2)))
