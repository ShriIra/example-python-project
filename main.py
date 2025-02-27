class Dog:
    legs = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f'{self.name} says: Bark!')


class SmallDog(Dog):
    def speak(self):
        print(f'{self.name} says: I can not bark')

    def whatsYourAge(self):
        print(f"{self.name} says: I am {self.age} years old")


class TinyDog(SmallDog):
    pass


dog = Dog("REX", 5)
dog.speak()
# dog.whatsYourAge()

smallDog = SmallDog("LUCY", 2)
smallDog.speak()
smallDog.whatsYourAge()


tinyDog = TinyDog("TINY", 1)
tinyDog.speak()
tinyDog.whatsYourAge()