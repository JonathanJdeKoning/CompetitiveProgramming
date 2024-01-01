volume = 7

shouts = int(input())

for _ in range(shouts):
    shout = input()
    
    if shout == "Skru op!" and volume < 10:
        volume += 1
    elif shout == "Skru ned!" and volume > 0:
        volume -= 1
print(volume)