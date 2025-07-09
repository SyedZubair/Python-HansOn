class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_price(self):
        return self.price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount_rate):
        super().__init__(name, price)
        self.discount_rate = discount_rate
    
    def get_price(self):
        return self.price * (1 - self.discount_rate)
    
regular = Product("Pen", 5)

print(f"Regular Price: ${regular.get_price()}")

discounted = DiscountedProduct("Pen", 5, 0.2)
print(f"Discounted Price: ${discounted.get_price()}")