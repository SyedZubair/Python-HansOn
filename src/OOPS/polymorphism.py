class Product:
    #constructor
    def __init__(self, quantity, price, name):
        self.quantity = quantity
        self.price = price
        self.name = name
    
    def get_discount(self):
        return 0
    

#electronic
class Electronics(Product):
    def get_discount(self):
        return self.price * 0.1
    
#clothing

class Clothing(Product):
    def get_discount(self):
        return self.price * 0.2
    #quantity=98,price=400,name="iPhone"
items = [Electronics(1000, 400, "laptop"), Clothing(50,900,"jacket")]
for i in items:
    print("Product Name:",i.name)
    print("Product discount:",i.get_discount())