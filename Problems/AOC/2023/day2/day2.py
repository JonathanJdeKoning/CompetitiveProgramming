a,b,p={"red":12,"green":13,"blue":14},0,0
with open("input.txt","r") as f:
 for l in f.readlines():
  s,d,n={"red":0,"green":0,"blue":0},False,l.split(": ")
  i=int(n[0].strip("Game "))
  for g in[x.strip()for x in n[1].replace(";",",").split(",")]:
   m,c=[int(x)if x.isdigit()else x for x in g.split()]
   if m>a[c]:d=True
   if m>s[c]:s[c]=m
  p+=(s["red"]*s["green"]*s["blue"])
  if d:continue
  b+=i
print(f"{b}\n{p}")
