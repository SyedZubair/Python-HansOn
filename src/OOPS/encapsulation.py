class Product:
    #constructor
    def __init__(self, quantity, price, name):
        self.quantity = quantity
        self.__price = price #private variable
        self.name = name

    def get_price(self):
        return self.__price
    
    def set_price(self, newprice):
        if newprice > 0:
            self.__price = newprice
        else:
            print('price must be in non negative number')

item = Product(5,3.5,"anti-virus")
print("Product price: ", item.get_price())
item.set_price(5.6)

print("Product price: ", item.get_price())
item.set_price(-5.6)
print("Product price: ", item.get_price())
