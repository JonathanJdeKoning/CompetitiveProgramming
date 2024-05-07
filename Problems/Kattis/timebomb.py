
d={"******   ******     ":0,
   "          *****     ":1,
   "*** ** * ** ***     ":2,
   "* * ** * ******     ":3,
   "  ***  *  *****     ":4,
   "* **** * **** *     ":5,
   "****** * **** *     ":6,
   "    *    ******     ":7,
   "****** * ******     ":8,
   "* **** * ******     ":9}

mat = []
for _ in range(5):
    mat.append(list(input()))

mat = ["".join(x) for x in list(zip(*mat[::-1]))]
mat.append("     ")
num = ""
for i in range(0,len(mat),4):
    s = "".join(mat[i:i+4])
    try:
        num += str(d[s])
    except:
        num = 1
        break
num = int(num)
if num%6==0:
    print("BEER!!")
else:
    print("BOOM!!")
