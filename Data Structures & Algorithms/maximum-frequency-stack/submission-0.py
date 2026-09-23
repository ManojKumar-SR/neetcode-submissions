class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] = self.freq.get(val,0) + 1
    
    def pop(self) -> int:
        max_count = 0
        max_val = []
        pop_value = -1

        for val,count in self.freq.items():
            if count >= max_count:
                max_count = count
        
        for val,count in self.freq.items():
            if count == max_count:
                max_val.append(val)
        
        right = len(self.stack) - 1

        while right >= 0:
            if self.stack[right] in max_val:
                pop_value = self.stack.pop(right)
                self.freq[pop_value] -= 1
                break
            right -= 1
        
        

        return pop_value
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()