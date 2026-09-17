class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []

    def push(self, val: int) -> None:
        if self.arr and self.min[-1] < val:
            self.min.append(self.min[-1])
        else:
            self.min.append(val)
        self.arr.append(val)
        
        print(self.min)
        print(self.arr)

    def pop(self) -> None:
        self.arr.pop()
        self.min.pop()

    def top(self) -> int:
        return self.arr[-1]
        
    def getMin(self) -> int:
        return self.min[-1]

