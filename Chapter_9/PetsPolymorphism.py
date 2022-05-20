# Pets polymorphism
# Three classes, all with a different "speak" method

class Dog():
    def __init__(self, name):
        #  Instance variables
         self.name = name
    
    def speak(self):
        print(self.name, 'say bark, bark, bark!')


class Cat():
    def __init__(self, name):
        #  Instance variables
         self.name = name
    
    def speak(self):
        print(self.name, "says , meeeooow")


class Bird():
    def __init__(self, name):
        #  Instance variables
         self.name = name
    
    def speak(self):
        print(self.name, "says , Tweet")


oDog1 = Dog("Rover")
oDog2 = Dog("Fido")
oCat1 = Cat("Fluffy")
oCat2 = Cat("Spike")
oBird = Bird("Big Bird")

pets_list = [oDog1, oDog2, oCat1, oCat2, oBird]


for oPet in pets_list:
    oPet.speak()
