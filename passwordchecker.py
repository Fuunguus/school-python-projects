import re

print("indtast dit password")

password = input()

passlenght = len(password)

min_length = 8

has_uppercase = False
has_digits = False
has_lowercase = False
has_special_chars = False

special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", ";", ":", "'", ",", ".", ">", "/", "?"]

while True:

    if not passlenght >= min_length:
        print("password too short")
        break

    elif not re.search('[A-Z]', password):
        print("Password missing uppercase")
        break

    elif not re.search('[a-z]', password):
        print("Password has no lowercase")
        break

    elif not re.search('[0-9]', password):
        print("Password has no numbers")
        break

    elif not special_chars:
        print("Password has no special characters")
        break

    else:
        print("Password good")
        break