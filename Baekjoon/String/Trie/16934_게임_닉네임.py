from collections import defaultdict
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key):
        self.key = key
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)
        self.keys = defaultdict(int)
    
    def insert(self, string):
        curr_node = self.head
        ans = 0

        for i, char in enumerate(string):
            if char in curr_node.children:
                ans = i + 1
            else:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        
        self.keys[string] += 1
        if ans == len(string) and self.keys[string] > 1:
            return f"{string}{self.keys[string]}"
        else:
            return string[:min(len(string), ans + 1)]

trie = Trie()
n = int(input())

for _ in range(n):
    print(trie.insert(input().rstrip()))