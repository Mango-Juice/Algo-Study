#트라이 구현
#https://leetcode.com/problems/implement-trie-prefix-tree


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if not i in node.children.keys():
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_word = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if not i in node.children.keys():
                return False
            node = node.children[i]
        return node.is_word
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if not i in node.children.keys():
                return False
            node = node.children[i]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
