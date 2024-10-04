is_number = True
while is_number:
    try:
        age = int(input("what is your age ? "))
        print(age)
        is_number = False
    except:
        print("please provide a number !")
