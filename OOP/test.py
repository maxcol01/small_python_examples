class User:
    def __init__(self, email):
        self.email = email


def sign_in(self):
    print("logged in")


def attack(self):
    pass


# note there is no constructor here since we might not want to haver attributes to the class

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attack with {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attack with {self.num_arrows}")


wizard = Wizard(name="Merlin", power=50)
archer = Archer(name="robin", num_arrows=100)


def player_attack(char: User) -> None:
    char.attack()


print(wizard.email)
