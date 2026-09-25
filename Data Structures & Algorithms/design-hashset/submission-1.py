class MyHashSet:

    def __init__(self):
        self.hashlist = []


    def add(self, key: int) -> None:
        if key not in self.hashlist:
            self.hashlist.append(key)

    def remove(self, key: int) -> None:
        
        for i in range(len(self.hashlist)):
            if self.hashlist[i] == key:
                del self.hashlist[i]
                break


    def contains(self, key: int) -> bool:
        if key in self.hashlist:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)