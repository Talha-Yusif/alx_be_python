class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

# Using polymorphism
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()

Cat.sound(Animal)
s=Animal()
s.sound()
p=Cat()
p.sound()
