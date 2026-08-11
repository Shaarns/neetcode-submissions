class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        
        if self.min_stk:
            min_val = min(self.min_stk[-1], val)
            self.min_stk.append(min_val)
        else:
            self.min_stk.append(val)

    def pop(self) -> None:
        if not self.stk:
            return None
        
        if self.min_stk:
            self.min_stk.pop()

        return self.stk.pop()
        
    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        if self.min_stk:
            return self.min_stk[-1]
        return 0
        
