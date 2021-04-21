#원형 큐 디자인
#https://leetcode.com/problems/design-circular-queue


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.front = 0
        self.rear = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == len(self.q):
            return False
        else:
            self.rear = (self.rear + 1) % len(self.q)
            self.q[self.rear] = value
            self.size += 1
            if self.size == 1:
                self.front = self.rear
            return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        else:
            self.q[self.front] = -1
            self.front = self.front + 1 if self.front < len(self.q) - 1 else 0
            self.size -= 1
            return True

    def Front(self) -> int:
        return self.q[self.front]

    
    def Rear(self) -> int:
        return self.q[self.rear]
        

    def isEmpty(self) -> bool:
        return self.size == 0

        
    def isFull(self) -> bool:
        return self.size == len(self.q)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
