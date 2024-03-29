       


class TrieNode:
    def __init__(self, val=None, children=[], isEnd=False):
        self.val = val
        self.next = next
        self.isEnd = isEnd

class Trie:
    def __init__(self,children=[]):
        self.children = children
        self.head = TrieNode
        return head

    def insert(self, word=None):
        dummy = self.head
        for c in word:
            next = TrieNode(val=c)
            dummy.children.append(next)
            dummy = next
        dummy.isEnd = True

myTrie = Trie
myTrie.insert("jonathan")



