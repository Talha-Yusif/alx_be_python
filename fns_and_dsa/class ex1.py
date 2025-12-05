"""
name=input("what is your name")
age=int(input("what is your age"))
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"the name of the studnt is {self.name}")
        print(f"the age of the studnt is {self.age}")
    


p=student(name,age)
p.info()
"""
name=input("what is the name of the product ")
price=int(input("what is the price of product "))
quantity=int(input('how many products are in stock '))
class product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def value(self):
        value=self.price*self.quantity
        print(f'the total value of {self.name} in stock is {value}')
poo=product(name,price,quantity)
poo.value()