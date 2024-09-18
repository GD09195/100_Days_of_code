class Animal:
    def __init__(self):
        self.eyes = 2
        self.alive = True

    def breath(self)-> None:
        print("Breathing...")

class Fish (Animal):
    def __init__(self):
        super().__init__()

    def breath(self) -> None:
        super().breath()
        print("...Underwater")

    def swim(self)-> None:
        print("Swimming...")


nemo = Fish()
nemo.swim()
nemo.breath()
print(f"Number of eyes: {nemo.eyes}")
print(f"Alive: {nemo.alive}")
