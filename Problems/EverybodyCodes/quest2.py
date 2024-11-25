# Part 1
words = ["LOR","LL","SI","OR","IU","UT","CI"]
s = "LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT, SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA. UT ENIM AD MINIM VENIAM, QUIS NOSTRUD EXERCITATION ULLAMCO LABORIS NISI UT ALIQUIP EX EA COMMODO CONSEQUAT. DUIS AUTE IRURE DOLOR IN REPREHENDERIT IN VOLUPTATE VELIT ESSE CILLUM DOLORE EU FUGIAT NULLA PARIATUR. EXCEPTEUR SINT OCCAECAT CUPIDATAT NON PROIDENT, SUNT IN CULPA QUI OFFICIA DESERUNT MOLLIT ANIM ID EST LABORUM."
print(sum([s.count(x) for x in words]))

# Part 2
words = ["MKLV","RJM","UJ","HC","HRVHAPXEWJ","B","ECVJBLWUWC","FDNR","DJWWWGLXOE","MA","AU","BGF","UVP","NSAEXQJMDQ","OP","CVNV","GUBS","CYYJ","UV","HMEA","K","QVL","HELYQCSFSM","ILZ","H","CXQV","MC","AAX","BUF","G","IJI","OW","WOW","JA","BCWN","BQKUHXPMUT","CEUS","VJRDIAJBEL","D","AJGNTYDTBO","OLJNVBCRBM","JTO","XDRB","VE","GD","HICWZSDUIH","XMZ","OO"]
symb = set()
with open("in/quest2pt2.in", "r") as file:
    for i,line in enumerate(file.readlines()):
        for word in words:
            if len(word) > len(line): continue
            l = 0
            r = len(word)
            while True:
                if line[l:r] == word or line[l:r] == word[::-1]:
                    for j in range(l,r):
                        symb.add((i,j))
                l += 1
                r += 1
                if r == len(line) +1:
                    break
print(len(symb))

# Part 3
scales = set()
words = ['DOI', 'FA', 'BSOEKJAYYY', 'QH', 'IY', 'OB', 'XGOQ', 'AVRC', 'YYD', 'FCPT', 'HMEDBOMUEF', 'EXR', 'GRO', 'VEWG', 'DGU', 'N', 'DRVJJNOHQQ', 'WHYZRNSSFV', 'LO', 'LL', 'ARDO', 'A', 'VOJ', 'VTAS', 'ZGX', 'QCH', 'TYCUDPOATQ', 'HBRA', 'GKG', 'YNIG', 'UCNMNOPGGA', 'DA', 'AWVOXUARWG', 'EKKCXJDKRY', 'RWFKQGNGGE', 'QKDTWFOGDY', 'QSKHCGEDQW', 'KK', 'OO', 'KO', 'BW', 'UB', 'HS', 'NHAI', 'H', 'QBM', 'B', 'MPQB', 'BKF', 'XE', 'BFFUHBXPJJ', 'HZCR', 'UO', 'ZANK', 'IFOI', 'I', 'VU', 'MTHC', 'WKAJ', 'IHEXZAHDBR', 'WOF', 'VFEQ', 'BQ', 'SFN', 'CKQWFSPZYJ', 'Z', 'JKC', 'KUMV', 'CCLGGGNDPY', 'VWE', 'DVP', 'SB', 'D', 'UF', 'EXQJMNKYUT', 'POTQUXWTSY', 'SGF', 'MOTNQHJHIR', 'M', 'LOL', 'YQJ', 'VQ', 'T', 'CT', 'MCIO', 'RFJMWKUOSU', 'MU', 'LRV', 'G', 'DRCJLHJIPG', 'POMP', 'CXQ', 'LJSD']
mat = []
with open("in/quest2pt3.in", "r") as file:
    for line in file.readlines():
        mat.append(list(line))
