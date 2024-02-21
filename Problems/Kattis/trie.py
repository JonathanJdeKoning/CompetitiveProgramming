
class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
        self.count = 0 


class Trie:
    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):
        return TrieNode()
        
        
    def _charToIndex(self,ch):
        return ord(ch)-ord('a')
        
        
    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
 
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
 
        pCrawl.isEnd = True
        pCrawl.count += 1

    def count_prefix(self, pref):
        crawl = self.root
        length = len(pref)
        for level in range(length):
            index = self._charToIndex(pref[level])

            if not crawl.children[index]:
                return 0
            else:
                crawl = crawl.children[index]
        pref_search = crawl
        def dfs(node):
            total = 0
            if node.isEnd: total += node.count
            childs = [x for x in node.children if x != None]
            if not any(childs): return total

        
            for child in childs:
                total += dfs(child)
            return total
        return dfs(pref_search)




t = Trie()
for _ in range(int(input())):
    word = input()
    print(t.count_prefix(word))
    t.insert(word)
    
    
