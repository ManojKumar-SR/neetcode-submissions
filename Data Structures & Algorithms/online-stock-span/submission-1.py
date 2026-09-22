class StockSpanner:

    def __init__(self):
        self.stock = []
        self.span = []

    def next(self, price: int) -> int:
        if len(self.stock) == 0:
            self.span.append(1)
        else:
            temp = 1
            while self.stock and self.stock[-1] <= price:
                temp += self.span.pop()
                self.stock.pop()
            self.span.append(temp)
        self.stock.append(price)
        return self.span[-1]
            
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)