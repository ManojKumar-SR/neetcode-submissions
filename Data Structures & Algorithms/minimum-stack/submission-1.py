class MinStack:
    minstack = []

    def __init__(self):
        self.stack = []
        self.minimum = 0

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minimum = val
        else:
            if val < MinStack.minstack[-1]:
                self.minimum = val
            else:
                self.minimum = MinStack.minstack[-1]
        MinStack.minstack.append(self.minimum)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        MinStack.minstack.pop()

        if len(self.stack) == 0:
            self.minimum = 0
        
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return MinStack.minstack[-1]