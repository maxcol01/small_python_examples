class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self) -> None:
        print("run")


player1 = PlayerCharacter("Toto")
player2 = PlayerCharacter("kiki")
print(player1.name)
player1.run()

player2.attack = 50

print(player1)
print(player2)


print(player2.attack)
help(player2)
