#스택을 이용한 큐 구현
#https://leetcode.com/problems/implement-queue-using-stacks

from collections import deque

class MyQueue:

    def __init__(self):
        self.stack = deque()
        

    def push(self, x: int) -> None:
        new_stack = deque([x])
        
        for i in self.stack:
            new_stack.append(i)
            
        self.stack = new_stack
        

    def pop(self) -> int:
        return self.stack.pop()
        

    def peek(self) -> int:
        return self.stack[-1]
        

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
