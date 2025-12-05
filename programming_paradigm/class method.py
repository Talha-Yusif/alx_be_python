class Dog:
    breed="bulldog"
    def __init__(self,name):
        self.name=name
    
    @classmethod
    def change_breed(cls,new_name):
        cls.breed=new_name
    
    def show_info(self):
        print(f"{self.name} is a {self.breed}")
dog1=Dog('Buddy')
dog1.show_info()
Dog.change_breed("pool")
dog1.show_info()
dog2=Dog("late")
dog2.show_info()
dog2.change_breed("German Shepperd")
dog2.show_info()