# Create an @authenticated decorator
# that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper_fn(*args, **kwargs):
        if args[0]["valid"]:
            fn(args)
        else:
            print("Invalid PW !")

    return wrapper_fn


@authenticated
def message_friends(user):
    print('message has been sent')


a = message_friends
a(user1)

