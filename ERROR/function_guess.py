import random as r


def guess_number(num: int, to_guess: int) -> str:
    try:
        if isinstance(num, int) and to_guess == num:
            return "Whoa you are a genius !"

    except ValueError:
        print("please provide a number !")


is_number = True
number_to_guess = r.randint(0, 10)
while is_number:
    age = int(input("Guess a number between 0 and 10 ? "))
    answer = guess_number(age, number_to_guess)
    if answer:
        print(answer)
        is_number = False
