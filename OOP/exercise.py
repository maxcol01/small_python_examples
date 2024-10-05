# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def oldest(*args: Cat) -> tuple:
    list_name = list()
    list_age = list()
    for cat in args:
        list_name.append(cat.name)
        list_age.append(cat.age)
    list_zipped = zip(list_name, list_age)
    return sorted(list_zipped)[-1]


# 1 Instantiate the Cat object with 3 cats

cat1: Cat = Cat(name="Mickey", age=5)
cat2: Cat = Cat(name="Minnie", age=7)
cat3: Cat = Cat(name="Donald", age=2)

# 2 Create a function that finds the oldest cat

oldest_cat = oldest(cat1, cat2, cat3)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {oldest_cat[1]}  years old")