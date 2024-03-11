class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        need = defaultdict(int)
        for c in target:
            need[c] += 1
        
        have = defaultdict(int)
        for c in s:
            if c in target:
                have[c] += 1
        if len(need) != len(have): return 0
        
        need = dict(sorted(dict(need).items()))
        have = dict(sorted(dict(have).items()))
        print(need)
        print(have)
        mx = math.inf
        for k,v in have.items():
            mx = min(mx, v//need[k])
        return mx
            
