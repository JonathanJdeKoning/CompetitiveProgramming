class Solution:
    @cache
    def countAndSay(self, n: int) -> str:
        def cas(n):
            if n == 1: return "1"
            s = cas(n-1)
            new = []
            for k,v in groupby(s):
                new.append(len(list(v)))
                new.append(list(k)[0])
            return "".join([str(x) for x in new])
        return cas(n)
        
            
