

string = input()
ts = string.count("T")
cs = string.count("C")
gs = string.count("G")
print((ts*ts+cs*cs+gs*gs)+ 7*min([ts,gs,cs]))