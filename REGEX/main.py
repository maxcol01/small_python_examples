import re


def password_checker(pw: str) -> (bool, str):
    # Define the allowed conditions
    length_check = r'^.{8}$'  # Password must be between 8 and 20 characters long
    uppercase_check = r'[A-Z]'  # At least one uppercase letter
    lowercase_check = r'[a-z]'  # At least one lowercase letter
    special_char_check = r'[!@#$%^&*(),.?":{}|<>]'  # At least one special character

    # check the good input

    if not isinstance(pw, str):
        print("Enter a string as a password")
    else:
        # Check the length of the password
        if not re.match(length_check, pw):
            return "Password must be  8 characters long."

        # Check for at least one uppercase letter
        if not re.search(uppercase_check, pw):
            return "Password must contain at least one uppercase letter."

        # Check for at least one lowercase letter
        if not re.search(lowercase_check, pw):
            return "Password must contain at least one lowercase letter."

        # Check for at least one special character
        if not re.search(special_char_check, pw):
            return "Password must contain at least one special character."

        return True


# Example usage
password = "helloER@"
print(password_checker(password))
