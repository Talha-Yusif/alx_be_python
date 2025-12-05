class Battery:
    def __init__(self,capacity,brand):
        self.capacity=capacity
        self.brand=brand
    def get_spec(self):
        return f"Brand: {self.brand}, Capacity: {self.capacity}"
class Camera:
    def __init__(self,megapixel,type):
        self.megapixel=megapixel
        self.type=type
    def get_spec(self):
        return f" Camera: {self.megapixel}MP , {self.type}"

class Phone:
    def __init__(self,model,battery,camera):
        self.model=model
        self.battery=battery
        self.camera=camera
    def phone_specs(self):
        print(f"Phone specs are {self.battery.get_spec()} and {self.camera.get_spec()}")

battery1=Battery(2000,"nokia")
camera1=Camera(56,'kloo')
phone=Phone("samsung",battery1,camera1)

phone.phone_specs()