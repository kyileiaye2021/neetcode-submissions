class MyHashSet:

    def __init__(self):
        self.myset = []
        

    def add(self, key: int) -> None:
        if key not in self.myset:
            self.myset.append(key)

    def remove(self, key: int) -> None:
        i, j = 0, 0
        while j < len(self.myset):
            if self.myset[j] != key:
                self.myset[i] = self.myset[j]
                i += 1
            j += 1
        self.myset = self.myset[:i]


    def contains(self, key: int) -> bool:
        return key in self.myset
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)