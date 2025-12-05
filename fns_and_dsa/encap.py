
class Laptop:
    def __init__(self,price):
        self.__price=price
    def get_price(self):
        return self.__price
    def set_price(self,new_price):
        if new_price>0:
            self.__price+=new_price
        else:
            print("Invalid price")
p=Laptop(50)
p.get_price()
p.set_price(30)
print(p.get_price())