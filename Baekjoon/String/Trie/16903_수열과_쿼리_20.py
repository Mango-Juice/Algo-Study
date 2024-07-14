import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.value = None
        self.count = 0
        self.left = None
        self.right = None


def insert(number):
    now = root
    for i in range(31):
        if number & (1 << 30 - i):
            if not now.right:
                now.right = Node()
            now = now.right
        else:
            if not now.left:
                now.left = Node()
            now = now.left
        now.count += 1
    now.value = number


def delete(number):
    now = root
    for i in range(31):
        if number & (1 << 30 - i):
            now = now.right
        else:
            now = now.left
        now.count -= 1


def find(number):
    now = root
    for i in range(31):
        if now.left == None or now.left.count <= 0:
            now = now.right
        elif now.right == None or now.right.count <= 0:
            now = now.left
        else:
            now = now.left if number & (1 << 30 - i) else now.right
    return now.value


root = Node()
insert(0)
n = int(input())
for _ in range(n):
    command, number = map(int, input().split())
    if command == 1: insert(number)
    elif command == 2: delete(number)
    else: print(number ^ find(number))