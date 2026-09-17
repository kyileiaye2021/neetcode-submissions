class MyHashMap:

    def __init__(self):
        self.key_arr = []
        self.val_arr = []

    def put(self, key: int, value: int) -> None:
        if key not in self.key_arr:
            self.key_arr.append(key)
            self.val_arr.append(value)

        else:
            for i, k in enumerate(self.key_arr):
                if k == key:
                    self.val_arr[i] = value


    def get(self, key: int) -> int:
        for i, k in enumerate(self.key_arr):
            if k == key:
                return self.val_arr[i]
        return -1
        

    def remove(self, key: int) -> None:
        i = 0
        for j, k in enumerate(self.key_arr):
            if k != key:
                self.key_arr[i] = self.key_arr[j]
                self.val_arr[i] = self.val_arr[j]
                i += 1

        self.key_arr = self.key_arr[:i]
        self.val_arr = self.val_arr[:i]
    

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)