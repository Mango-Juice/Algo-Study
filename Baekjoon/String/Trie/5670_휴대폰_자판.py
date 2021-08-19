# https://www.acmicpc.net/problem/5670

from collections import deque
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key = None, data = None, count = 0):
        self.key = key
        self.data = data
        self.count = count
        self.children = {}

    def __lt__(self, other):
        if self.key == None or other.key == None: return True
        return self.key < other.key

class Trie:
    def __init__(self):
        self.root = Node()

    def append(self, string):
        now = self.root

        for char in string:
            if not char in now.children:
                now.children[char] = Node(char)
            now.count += 1
            now = now.children[char]

        if now.key != None:
            now.count += 1

        now.data = string

    def getValue(self, string):
        now = self.root
        result = 0

        for char in string:

            if now == self.root or now.data != None or len(now.children) > 1:
                result += 1
            
            now = now.children[char]
                    
            if now.count == 1:
                return result

        return result + (1 if now.count == 1 else 0)


while True:
    try:
        tree = Trie()
        arr = []
        answer = 0
        
        for _ in range(int(input())):
            inp = input().rstrip()
            tree.append(inp)
            arr.append(inp)

        for i in arr:
            val = tree.getValue(i)
            answer += val

        print(f"{answer / len(arr):.2f}")

    except:
        break
