# https://www.acmicpc.net/problem/14725

from collections import deque
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key = None, data = None):
        self.key = key
        self.data = data
        self.children = {}

    def __lt__(self, other):
        if self.key == None or other.key == None: return True
        return self.key < other.key

class Trie:
    def __init__(self):
        self.root = Node()

    def append(self, words):
        now = self.root

        for word in words:
            if not word in now.children:
                now.children[word] = Node(word)
            now = now.children[word]

        now.data = words

    def print(self):
        stack = deque([(self.root, -2)])

        while stack:
            target, count = stack.pop()
            
            if target.key != None:
                print('-' * count + target.key)
            
            for i in sorted(target.children.values(), reverse = True):
                stack.append((i, count + 2))


tree = Trie()
n = int(input())

for _ in range(n):
    tree.append(input().split()[1:])

tree.print()
