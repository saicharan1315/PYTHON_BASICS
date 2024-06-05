class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, lang):
        print(f"Hi my name is {self.name} and my age is {self.age} and my language is {lang}")


sai = Person(name="SAI", age=20)
charan = Person(name="CHARAN", age=21)

sai.speak("Telugu")