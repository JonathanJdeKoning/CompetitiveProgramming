
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
ans1 = 0
ans2 = 0
from copy import copy
with open("day4.in", "r") as file:
    mp = {}
    for i, x in enumerate(file.readlines()):
        line = x.strip()
        if line != "":
            for data in line.split():
                k,v = data.split(":")
                mp[k] = v
        else:
            for field in fields:
                if field not in mp:
                    break
            else:
                ans1 += 1
                bad = False
                try:
                    byr = int(mp["byr"])
                    iyr = int(mp["iyr"])
                    eyr = int(mp["eyr"])
                    hgt = mp["hgt"]
                    hcl = mp["hcl"]
                    ecl = mp["ecl"]
                    pid = mp["pid"]

                    if byr < 1920 or byr > 2002: bad = True
                    if iyr < 2010 or iyr > 2020: bad = True
                    if eyr < 2020 or eyr > 2030: bad = True
                    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: bad = True
                    if not (len([x for x in pid if x.isdigit()]) == 9 and len(pid)==9): bad = True
                    if hcl[0] != "#": bad = True 
                    if len(hcl) != 7: bad = True
                    if len([c for c in hcl[1:] if c in "1234567890abcdef"]) != 6: bad = True
                    if hgt[-2:] not in ["cm", "in"]: bad = True
                    v = hgt[:-2]
                    if len([x for x in v if not x.isdigit()]): bad = True
                    v = int(v)
                    if hgt[-2:] == "cm":
                        if v <150 or v >193: bad = True
                    else:
                        if v < 59 or v > 76: bad = True
                except:
                    bad = True
                if not bad:
                    ans2 += 1

            mp = {}

print(ans1)
print(ans2)

