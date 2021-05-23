#팰린드롬 페어
#https://leetcode.com/problems/palindrome-pairs


from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.children = defaultdict(TrieNode)
        self.palins = []
        self.val = ''


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]
        
    def insert(self, index: int, word: str) -> None:
        node = self.root
        for i, c in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palins.append(index)
            node = node.children[c]
            node.val = c
        node.word_id = index
        
    def search(self, index: int, word: str) -> List[List[int]]:
        node = self.root
        result = []
        
        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
        
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
            
        for p in node.palins:
            result.append([index, p])
        
        return result

    
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        answer = []
        
        for i, j in enumerate(words):
            trie.insert(i, j)
            
        for i, j in enumerate(words):
            answer.extend(trie.search(i, j))
            
        return answer
