import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    else:
        return False

user_input = input("Enter an email address: ")


if validate_email(user_input):
    print(f"The email '{user_input}' is a valid email address.")
else:
    print(f"The email '{user_input}' is not a valid email address.")

    