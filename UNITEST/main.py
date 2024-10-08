def do_stuff(number: int) -> int:
    try:
        return int(number) + 5
    except ValueError:
        print("Please enter a number !")
