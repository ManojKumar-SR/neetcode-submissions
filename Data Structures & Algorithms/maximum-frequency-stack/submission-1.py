class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stack = {}
        self.maxi = 0

    def push(self, val: int) -> None:
        count = self.freq.get(val,0) + 1
        self.freq[val] = count
        
        if count > self.maxi:
            self.maxi = count
            self.stack[self.maxi] = []
        
        self.stack[count].append(val)

    def pop(self) -> int:
        pop_ele = self.stack[self.maxi].pop()

        if not self.stack[self.maxi]:
            self.maxi -= 1
        
        self.freq[pop_ele] -= 1

        return pop_ele

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()