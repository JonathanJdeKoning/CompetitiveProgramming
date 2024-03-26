class Solution:
    def oddString(self, words: List[str]) -> str:
        diffs = []
        for word in words:
            diff = []
            for i in range(len(word)-1):
                diff.append(ord(word[i+1])-ord(word[i]))
            diffs.append(diff)
        print(diffs)
        a = diffs[0]
        b = diffs[1]
        if a==b:
            for i,diff in enumerate(diffs[2:],start=2):
                if diff != a: 
                    return words[i]
        else:
            if diffs[2] != a:
                return words[0]
            return words[1]



                
