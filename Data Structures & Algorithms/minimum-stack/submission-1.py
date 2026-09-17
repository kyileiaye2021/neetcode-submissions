class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        print(self.arr)
        
    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]
        
    def getMin(self) -> int:
        min_ele = float('inf')
        for ele in self.arr:
            min_ele = min(min_ele, ele) 

        return min_ele

