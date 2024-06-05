class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def description(self):
        print(f"This is {self.name} is cute and he is {self.age} old. His breed is {self.breed}")

class Parrot(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def description(self):
        print(f"This is {self.name} is a {self.color} parrot and she is {self.age} old.")

dog = Dog("yuvraj", 5, "pomerian")
animal = Animal("leo", 3)
parrot = Parrot("cutie", 2, "pink")

dog.description()
parrot.description()