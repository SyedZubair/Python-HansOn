class Product:

    #memeber variable
    #quantity = 0

    #constructor
    def __init__(self, quantity, price, name):
        self.quantity = quantity
        self.price = price
        self.name = name

    #function // memeber function
    def total_value(self):
        return self.quantity * self.price

#object 
item = Product(quantity=98,price=400,name="iPhone")
print("total value of the product: ",item.total_value())

item2 = Product(quantity=102,price=200,name="android")
print("total value of the product: ",item2.total_value())