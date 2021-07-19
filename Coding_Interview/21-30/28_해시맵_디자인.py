#해시맵 디자인
#https://leetcode.com/problems/design-hashmap


class MyHashMap:

    def __init__(self):
        self.dic = {}

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value

    def get(self, key: int) -> int:
        if not key in self.dic.keys():
            return -1
        return self.dic[key]
        
    def remove(self, key: int) -> None:
        if not key in self.dic.keys():
            return
        del self.dic[key]
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
