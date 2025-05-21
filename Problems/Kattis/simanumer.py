class Trie:
    def __init__(self, words):
        self.root = {}
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                current_dict[letter] = {"count": 0 }
            current_dict = current_dict[letter]
            current_dict["count"] += 1

    def count_pref(self, pref):
        current_dict = self.root
        for letter in pref:
            if letter not in current_dict: return 0 
            current_dict = current_dict[letter]
        return current_dict["count"]
N = int(input())
words = [input() for _ in range(N)]
trie = Trie(words)
q = int(input())
for _ in range(q):
    print(trie.count_pref(input()))