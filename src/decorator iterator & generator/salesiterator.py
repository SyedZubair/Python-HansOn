class SalesIterator:

    def __init__(self, sales):
        self.sales = sales
        self.index =0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.sales):
            result = self.sales[self.index]
            self.index += 1
            return result
        raise StopIteration
    
sales_data = SalesIterator([100, 200, 300, 400])
for sale in sales_data:
    print(f"Sale: ${sale}")