class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Meow!")