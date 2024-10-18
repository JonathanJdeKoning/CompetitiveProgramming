mp = {0: "Monday" ,1:"Tuesday", 2: "Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
d, m = list(map(int, input().split()))
y = 2009

import datetime
a = datetime.datetime(2009, m, d)
print(mp[a.weekday()])