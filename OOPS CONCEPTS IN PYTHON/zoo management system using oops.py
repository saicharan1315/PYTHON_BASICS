class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} named {self.name} goes '{self.sound}'")

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion", "roar")

    def get_info(self):
        print("Lions are the king of the jungle.")


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "Elephant", "trumpet")

    def get_info(self):
        print("Elephants are the largest land animals.")


class Snake(Animal):
    def __init__(self, name):
        super().__init__(name, "Snake", "hiss")

    def get_info(self):
        print("Snakes can be found on every continent except Antarctica.")


leo = Lion("Leo")
ellie = Elephant("Ellie")
slyther = Snake("Slyther")

leo.make_sound()
leo.get_info()
print()
.
ellie.make_sound()
ellie.get_info()
print()

slyther.make_sound()
slyther.get_info()
print()
