
class chair:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(name)
    #def __del__(self):
        #print(f'{self.name} and {self.age} are no more')


    
poo=chair("Talha",56)
del poo
#print(poo.age)   
