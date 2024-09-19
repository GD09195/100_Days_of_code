from random import randint

class User:

    def __init__(self, username) -> None:
        self.id = randint(0,100)
        self.username = username

userA = User("gd0912")

print(userA.id, userA.username)