# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return (c * 9/5) + 32

#     @staticmethod
#     def fahrenheit_to_celsius(f):
#         return (f - 32) * 5/9

#     @staticmethod
#     def convert_celsius_list(c_list):
#         # Converts a list of Celsius values to Fahrenheit
#         return [TemperatureConverter.celsius_to_fahrenheit(c) for c in c_list]

#     @staticmethod
#     def convert_fahrenheit_list(f_list):
#         # Converts a list of Fahrenheit values to Celsius
#         return [TemperatureConverter.fahrenheit_to_celsius(f) for f in f_list]
# p=[0,34,65,45]
# r=TemperatureConverter.convert_celsius_list(p)
# print(r)
# class Animal:
#   def make_sound(self):
#     print("Generic animal sound")

# class Dog(Animal):
#   def make_sound(self):
#     print("Woof!")

# animals = [Dog(), Animal()]
# for animal in animals:
#   animal.make_sound()  
class Bird:
    def fly(self):
        print("fly with wings")

class Airplane:
    def fly(self):
        print("fly with fuel")

class Fish:
    def swim(self):
        print("fish swim in sea")

# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane(), Fish():
    obj.fly()