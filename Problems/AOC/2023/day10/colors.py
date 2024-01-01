from PIL import Image
from collections import Counter
im = Image.open("herewego.png")
greens = 0
print(Counter(list(im.getdata())))
for pixel in im.getdata():
    if pixel == (10,255,46):
        greens+= 1
print(greens)
