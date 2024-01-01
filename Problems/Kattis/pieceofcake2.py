len, hdist, vdist = list(map(int, input().split()))
thick = 4


sec1 = hdist*vdist
sec2 = (len-hdist)*vdist
sec3 = (len-vdist) * hdist
sec4 = (len-vdist) * (len - hdist)

big = max([sec1, sec2, sec3, sec4])

print(int(big*thick))
