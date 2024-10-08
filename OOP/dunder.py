class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": "Max",
            "age": 33
        }

    def __str__(self):
        return f"{self.color}"

    def __call__(self):
        return "HELOOOOOOO"

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy(color="red", age=0)
print(action_figure.__str__())
print(str(action_figure))
print(action_figure["name"])
