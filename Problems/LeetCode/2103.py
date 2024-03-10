class Solution:
    def countPoints(self, rings: str) -> int:
        rods = defaultdict(list)
        for i in range(0,len(rings),2):
            data = rings[i:i+2]
            rods[data[1]].append(data[0])
        return len([k for k,v in rods.items() if len(set(v)) == 3])
