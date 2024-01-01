string = input()

words = string.split()

ewcount = 0

for word in words:
    if "ae" in word:
        ewcount += 1
        
if ewcount/ len(words) >= 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")