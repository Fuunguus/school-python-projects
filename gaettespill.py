from random import randint

i = 1

tal = randint(1, 100)

print("spil? Y // N")

if "Y" in input():
    answer = 1

else:
    answer = 0

while answer != 0:

    for i in range(1, 10):

        print("nummer forsøg:", i)
        guess = int(input("Prøv igen teehee "))

        if guess == tal:
            print("tillykkeee!!! :DD")

        elif guess < 0 or guess > 100:
            print("damm du missede hårdt")

        elif abs(guess - tal) > 50:
            print("hahaha forkert")

        elif abs(guess - tal) > 19 and 49 > abs(guess - tal):
            print("close??")

        else:
            print("damm du dårlig xDDD")

    print("svaret var:")
    print(tal)

    print("prøv igen? Y // N")

    if "Y" in input():
        answer = 1

    else:
        answer = 0


"""
til sidst viser den det tal som du skulle have gættet
"""