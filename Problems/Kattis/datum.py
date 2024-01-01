monthdict = {
    1:1,
    2:4,
    3:4,
    4:0,
    5:2,
    6:5,
    7:0,
    8:3,
    9:6,
    10:1,
    11:4,
    12:6
}
weekdict = {
    2:"Saturday",
    3:"Sunday",
    4:"Monday",
    5:"Tuesday",
    6:"Wednesday",
    0:"Thursday",
    1:"Friday"
}
d,m = list(map(int, input().split()))
print(weekdict[((11+d+monthdict[m]+6+9)%7)])