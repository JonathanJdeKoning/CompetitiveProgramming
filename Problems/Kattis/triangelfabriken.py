a = int(input())
b = int(input())
c = int(input())
tri = [a,b,c]
if 90 in tri:
    print("Ratvinklig Triangel")
elif all(x < 90 for x in tri):
    print("Spetsig Triangel")
else:
    print("Trubbig Triangel")