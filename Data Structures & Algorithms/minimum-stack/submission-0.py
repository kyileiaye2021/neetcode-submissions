class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            curr_min = min(self.minStack[-1], val)
        else:
            curr_min = val
        self.minStack.append(curr_min)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return null

    def getMin(self) -> int:
        return self.minStack[-1]
