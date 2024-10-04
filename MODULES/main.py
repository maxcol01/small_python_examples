import random as rd
import sys

print("WELCOME TO THE GUESSING GAME !!!! ")

first = sys.argv[1]
end = sys.argv[2]

is_different = True

random_num = rd.randint(int(first), int(end))

while is_different:
    guess_user = int(input(f"Guess a number between {first} and {end}: "))
    if guess_user == random_num:
        print("CONGRATS ! YOU'RE A GENIUS ! You Won")
        is_different = False
